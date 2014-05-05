
import string
import random

import department
import user

from lib import socket

PRED_ORG_NAMES = [
    "Juniper"
]

PRED_ORG_LOCATIONS = {
    "New York": {
        "lat": 40.7127,
        "lng": -74.0059
    },
    'Los Angeles' : {
        "lat": 34.0500,
        "lng": -118.2500
    },
    'Chicago' : {
        "lat": 41.8819,
        "lng": -87.6278
    },
    'Phoenix': {
        "lat": 33.4500,
        "lng": -112.0667
    },
    'San Diego': {
        "lat": 32.7150,
        "lng": -117.1625
    },
    'San Jose': {
        "lat": 37.3333,
        "lng": -121.9000
    }
}

def emulate_org_list(settings, app_list, norgs=1):
    orgs = []

    for i in range(norgs):
        org = Org(settings, app_list)
        for user in org.user_list:
            user.org = org
            user.gen_app_info()
        orgs.append(org)

    return orgs

"""
    Org:
    An 'Org' class contains users, subscribed apps except its own information
    'vyatta_list': gw in this org

"""
class Org(object):
    def __init__(self, settings, app_list):
        self.settings = settings
        self.name = random.choice(PRED_ORG_NAMES)
        self.ndepartment = random.randint(3, 10)
        #self.departments = department.emulate_department_list(self.ndepartment)
        self.domain = self.name.lower() + ".com"
        self.app_list = {}

        self.n_loc = min(random.randint(settings['org']['nloc']['min'], settings['org']['nloc']['max']),
                         len(PRED_ORG_LOCATIONS.keys()))
        self.loc = random.sample(PRED_ORG_LOCATIONS.keys(), self.n_loc)

        " Subscribed apps "
        business_app_list = {}
        for key, value in app_list.items():
            if value.type == 'non-business':
                continue
            business_app_list[key] = value
        self.n_apps = random.randint(settings['org']['napps']['min'], settings['org']['napps']['max'])
        if self.n_apps >= business_app_list.keys():
            app_name_list = business_app_list.keys()
        else:
            app_name_list = random.sample(business_app_list.keys(), self.n_apps)

        for app_name in app_name_list if 'uncategoried' in app_name_list else (app_name_list + ['uncategoried']):
            self.app_list[app_name] = app_list[app_name]

        if 'box' not in self.app_list:
            self.app_list['box'] = app_list['box']

        " Users "
        self.nuser = random.randint(settings['org']['nemployees']['min'], settings['org']['nemployees']['max'])
        self.user_list = user.emulate_user_list(settings, self.app_list, self.nuser)

        " Vyatta "
        self.nvyatta = self.n_loc
        self.vyatta_list = self._fake_vyatta_list()

    def _fake_vyatta_list(self):
        vyattas = []
        for i in range(0, self.nvyatta):
            vyatta_loc = random.choice(self.loc)
            vyatta = {
                "id": ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)),
                "lat": PRED_ORG_LOCATIONS[vyatta_loc]['lat'],
                "lng": PRED_ORG_LOCATIONS[vyatta_loc]['lng'],
                "loc": vyatta_loc,
                "sockets": socket.gen_socket_list("private", "client", 200)
            }
            vyattas.append(vyatta)

        return vyattas
