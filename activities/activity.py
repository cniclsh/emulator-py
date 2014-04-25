import random

import tcpsess

import logging

logger = logging.getLogger('activity')

class Activity(object):

    def __init__(self, time_range, user, app, activity_name, data_length=None):
        self.user = user
        self.app = app
        self.activity_name = activity_name

        self.time_range = time_range
        self.data_length = data_length if data_length else random.randint(0, 9999)

        self.packet_list = self._gen_tcpsess().packet_list

    def _gen_tcpsess(self):

        client_socket = self.user.curr_socket
        server_socket = self.app.socket_list[self.app.curr_socket]

        tcp_sess = tcpsess.TcpSess(self.time_range,
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
            record['enterprise'] = self.user.org.name
            record['location'] = {"lat": self.user.vyatta['lat'],
                                  "lon":self.user.vyatta['lng']}
            record['type'] = self.app.type
            record['category'] = self.app.category
            record['risklevel'] = self.app.risklevel

            records.append(record)
        return records

    def logging_activity(self):
        record ={}

        client_socket = self.user.curr_socket
        server_socket = self.app.socket_list[self.app.curr_socket]
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
        return record

