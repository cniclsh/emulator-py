import random

import tcpsess

import logging

from users import org

logger = logging.getLogger('activity')

class Activity(object):

    def __init__(self, settings, time_range, user, app, activity_name, activity_setting=None):
        self.user = user
        self.app = app
        self.activity_name = activity_name

        self.time_range = time_range
        self.activity_setting = activity_setting
        self.data_length = activity_setting['data_length'] if activity_setting else random.randint(0, 9999)

        self.packet_list = self._gen_tcpsess(settings).packet_list

    def _gen_tcpsess(self, settings):

        client_socket = self.user.curr_socket
        server_socket = self.app.socket_list[self.app.curr_socket]

        tcp_sess = tcpsess.TcpSess(settings,
                                   self.time_range,
                                   self.user.vyatta,
                                   client_socket,
                                   server_socket,
                                   self.app.name,
                                   self.data_length)

        logger.info("time: (%s, %s), activity: %s, n_packet %d " % (self.time_range.str_begin,
                                                                    self.time_range.str_end,
                                                                    self.activity_name,
                                                                    len(tcp_sess.packet_list)))
        return tcp_sess

    def logging_tcpsess(self):
        records = []
        for packet in self.packet_list:
            record = packet.__dict__
            record['@timestamp'] = packet.timestamp
            del(record['timestamp'])
            record['enterprise'] = self.user.org.name
            record['geo'] = {"lat": self.user.vyatta['lat'],
                             "lon":self.user.vyatta['lng']}
            record['location'] = self.user.vyatta['loc']
            record['type'] = self.app.type
            record['category'] = self.app.category
            record['risklevel'] = self.app.risklevel
            record['department'] = self.user.depart

            records.append(record)
        return records

    def logging_activity(self):
        record ={}

        client_socket = self.user.curr_socket
        server_socket = self.app.socket_list[self.app.curr_socket]
        record['department'] = self.user.depart
        record['location'] = random.sample(org.PRED_ORG_LOCATIONS.keys(), 1)[0]
        record['vyatta'] = self.user.vyatta['id']
        record['srcip'] = client_socket.ipaddr
        record['srcport'] = client_socket.port
        record['dstip'] = server_socket.ipaddr
        record['dstport'] = server_socket.port
        record['appname'] = self.app.name
        record['size'] = self.data_length
        record['proto'] = 'TCP'
        record['time_begin'] = self.time_range.str_begin
        record['time_end'] = self.time_range.str_end
        record['browser'] = {
                                'family': self.user.user_agent.browser.family,
                                'version': self.user.user_agent.browser.version_string
                             }
        record['os'] = {
                                'family': self.user.user_agent.os.family,
                                'version': self.user.user_agent.os.version_string
                             }
        record['device'] = self.user.user_agent.device.family

        record['success'] = random.choice([False] * self.activity_setting['result']['failure'] + [True] * self.activity_setting['result']['success'])

        return record

