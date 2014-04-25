
import packet


PacketLogTemp = '{ \
"@timestamp":"%s", \
"vyatta": "%s", \
"dir": "%s", \
"srcip": "%s", \
"srcport": %d, \
"dstip": "%s", \
"dstport": %d, \
"appname": "%s", \
"proto": "TCP", \
"size": %d, \
"enterprise": "%s", \
"location": "%s", \
"risklevel": "%s", \
"type": "%s", \
"category": "%s" \
}'


class TcpSess(object):
    def __init__(self, time_range, vyatta, client_socket, server_socket, appname, content_length):
        self.vyatta = vyatta
        self.client_socket = client_socket
        self.server_socket = server_socket
        self.appname = appname
        self.content_length = content_length
        self.packet_list = packet.emulate_packet_list(time_range, vyatta, client_socket, server_socket, appname, content_length)


    def logging(self):
        pass

