
import random

TCPSESS_MIN_PACKETS = 8
PACKET_MIN_LENGTH = 52
PACKET_MAX_LENGTH = 1024


def emulate_packet_list(time_range, vyatta, client_socket, server_socket, appname, content_length):
    packets = []
    n_packet = max(TCPSESS_MIN_PACKETS, content_length/PACKET_MAX_LENGTH)
    sub_time_range = time_range.split(n_packet)
    for i in range(0, n_packet):
        timestamps = sub_time_range[i].get_points(2)
        """ client to Server """

        length = random.randint(PACKET_MIN_LENGTH, PACKET_MAX_LENGTH)
        packet = Packet(timestamps[0], vyatta, client_socket.ipaddr,
                        client_socket.port, server_socket.ipaddr,
                        server_socket.port, appname, 'up', length)
        packets.append(packet)

        """ server to client """
        length = random.randint(PACKET_MIN_LENGTH, PACKET_MAX_LENGTH)
        packet = Packet(timestamps[1], vyatta, server_socket.ipaddr,
                        server_socket.port, client_socket.ipaddr,
                        client_socket.port, appname, 'down', length)
        packets.append(packet)

    return packets


class Packet(object):
    def __init__(self, timestamp, vyatta, src_ip, src_port, dst_ip, dst_port, appname, direction, length, proto= 'TCP'):
        self.datetime = timestamp
        self.vyatta = vyatta['id']
        self.srcip = src_ip
        self.srcport = src_port
        self.dstip = dst_ip
        self.dstport = dst_port
        self.appname = appname
        self.dir = direction
        self.size = length
        self.proto = proto






