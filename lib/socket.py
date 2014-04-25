import random

HTTPS_SERVER_BASE = 10


def gen_socket_list(ip_type, port_type, nsocket=1):
    sockets = []
    for i in xrange(0, nsocket):
        sockets.append(Socket(ip_type, port_type))

    return sockets


class Socket(object):
    def __init__(self, ip_type='public', port_type='server'):
        if ip_type == 'public':
            self.ipaddr = str(random.randint(11, 120)) + "." \
                + str(random.randint(0, 127)) + "." \
                + str(random.randint(0, 127)) + "." \
                + str(random.randint(1, 254))
        else:
            self.ipaddr = "192.168." + str(random.randint(1, 120)) + "." + str(random.randint(1, 200))

        if port_type == 'server':
            self.port = random.choice([443] * HTTPS_SERVER_BASE + [80])
        else:
            self.port = random.randint(3097, 9999)