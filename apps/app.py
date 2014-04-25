import random

from lib import socket
import resource

def emulate_app_list(settings):
    apps = {}

    for appname, app in settings.iteritems():
        apps[appname] = App(appname, app)

    return apps


class App(object):
    def __init__(self, app_name, app_dict):
        self.name = app_name
        self.type = app_dict['type']
        self.category = app_dict['category']
        self.risklevel = app_dict['risklevel']
        self.socket_list = socket.gen_socket_list('public', 'server', app_dict['nips'])
        self.curr_socket = 99999
        self.resource = resource.Resource(app_name)

    def select_socket(self):
        self.curr_socket = random.randint(0, len(self.socket_list) - 1)



