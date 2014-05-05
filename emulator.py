__author__ = 'cniclsh'

"""
  Emulator:

  This package generates all kind of data for log visualization.
  The functions are as following:


  The emulated entities are as following:
  1. User:
  2. App:
  3. Activity:

"""

from apps import app
from users import org, user
import random
from activities import httpsess
from lib import timerange

from elasticsearch import Elasticsearch

import json
import os
import sys, getopt
from datetime import datetime, timedelta

import config_ini
import logging

import mappings

PROJECT_ROOT = os.getcwd()
SETTING_FILE = os.path.join(PROJECT_ROOT, "settings.json")
PREDEFINED_NAME_FILE = os.path.join(PROJECT_ROOT, "users/usernames")

logger = logging.getLogger(__name__)

def read_setting_from_file(file = SETTING_FILE):
    with open(file, 'rb') as fs:
        settings = json.loads(fs.read())

    return settings


def read_predefined_names():

    with open(PREDEFINED_NAME_FILE, 'rb') as fp:
        names = [ line.rstrip('\n').lower() for line in fp]

    return names


def create_es_index(es, timestamp, org, index_types=['gw', 'aie']):
    index_names = {}
    for index_type in index_types:
        index_name = org.name.lower() + '-' + index_type + '-' + datetime.fromtimestamp(timestamp).strftime('%Y.%m')

        mapping_dict, doc_type = (mappings.gw_mapping, 'tcpsession') if index_type == 'gw' else (mappings.aie_mapping, "activity")

        # create empty index
        es.indices.create(index=index_name, body='', ignore=400)
        #es.indices.put_mapping(index=index_name,
        #                       doc_type=doc_type,
        #                       body={
        #                           doc_type : {
        #                               "properties" : mapping_dict
        #                           }
        #                       }
        #)

        index_names[index_type] = index_name

    return index_names

class Emulator:
    def __init__(self, kdb_server, setting_file=SETTING_FILE):
        self.settings = read_setting_from_file(setting_file)
        self.kdb_server = kdb_server
        self.es = Elasticsearch(kdb_server)

        " Generate list of Org "
        self.app_list = app.emulate_app_list(self.settings['apps'])
        self.org_list = org.emulate_org_list(self.settings, self.app_list, self.settings['norgs'])

    """
        gen_org_traffic
    """
    def gen_org_traffic(self, org, begin_time, end_time):
        time_range = timerange.TimeRange(begin_time, end_time)

        logger.info("org: %s, official_app: (%s)" % (org.name, ", ".join(app_name for app_name in org.app_list.keys())))

        index_names = create_es_index(self.es, time_range.begin, org)
        logger.info("Create indexs: (%s, %s)" % tuple(index_names.values()))

        for user in org.user_list:

            app_name_list = random.sample(user.app_user_info.keys(), random.randint(user.n_personal_app, len(user.app_user_info.keys())))
            for app_name in app_name_list:
                n_packet, n_activity, http_sessions = httpsess.emulate_http_sessions(self.settings['sess'],
                                                               user,
                                                               self.app_list[app_name],
                                                               time_range)

                logger.info("%s: org: %s, user: %s, app: %s, http_sess: %d, activity: %d, packet: %d" % (begin_time, org.name, user.name, app_name, len(http_sessions), n_activity, n_packet))

                if self.settings['debug']:
                    continue

                for http_session in http_sessions:
                    if http_session['pkg']:

                        [self.es.index(index=index_names['gw'], doc_type='tcpsession', body=json.dumps(pkg_log)) for pkg_log in http_session['pkg']]

                    if http_session['app']:

                        [self.es.index(index=index_names['aie'], doc_type='activity', body=json.dumps(app_log)) for app_log in http_session['app']]

    def run(self, begin_time, end_time):
        for org in self.org_list:
            self.gen_org_traffic(org, begin_time, end_time)


if __name__ == '__main__':
    time_begin = ''
    time_end = ''
    kdb_server = '127.0.0.1'

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:b:e:", ["kdb_server=", "time_begin=", "time_end="])
    except getopt.GetoptError:
        print 'emulator.py -s <elasticsearch_server> -b <time_begin> -e <time_end>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'emulator.py -s <elasticsearch_server> -b <time_begin> -e <time_end>'
            sys.exit()
        elif opt in ("-s", "--kdb"):
            kdb_server = arg
        elif opt in ("-b", "--time_begin"):
            time_begin = arg
        elif opt in ("-e", "--time_end"):
            time_end = arg

    try:
        datetime_begin = datetime.strptime(time_begin, "%Y-%m-%d")
        datetime_end = datetime.strptime(time_end, "%Y-%m-%d")

    except Exception:
        print "Wrong time format! For example , '2014-04-23'"
        sys.exit(2)

    if datetime_begin > datetime_end:
        print "time_begin < time_end"
        sys.exit(2)

    user.PREDEFINED_USER_NAMES = read_predefined_names()

    emulator = Emulator(kdb_server)

    while datetime_begin <= datetime_end:

        emulator.run(datetime_begin.strftime("%Y-%m-%d"),
                     datetime_begin.strftime("%Y-%m-%d"))

        datetime_begin = datetime_begin + timedelta(days=1)


