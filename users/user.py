import random

import agent

PREDEFINED_USER_NAMES = []


def emulate_user_list(settings, official_app_list, nuser=1):
    users = []

    names = random.sample(PREDEFINED_USER_NAMES, nuser)

    for i in range(0, nuser):
        users.append(User(settings, names[i]))

    return users

"""
    User:
    The 'User' class contains user information, such as login info for each app,
    ip address.

"""
class User(object):
    def __init__(self, settings, name):
        self.settings = settings
        self.name = name
        self.n_personal_app = random.randint(settings['user']['napps']['min'], settings['user']['napps']['max'])

        self.app_user_info = {}

        self.org = None

        " Socket info should be confirmed during generating traffic "
        self.vyatta = None
        self.curr_socket = None

        self.user_agent = None

    def gen_app_info(self):
        if not self.org:
            raise Exception("org should be initialized")

        for app_name, app in self.org.app_list.iteritems():
            self.app_user_info[app_name] = {
                'login': self.name + "@" + self.org.domain,
                'user_id': random.randint(208118596, 308118596)
            }

        personal_app_list = list(set(self.settings['apps'].keys()) - set(self.org.app_list.keys()))
        for app_name in random.sample(personal_app_list, self.n_personal_app):
            self.app_user_info[app_name] = {
                'login': self.name + "@" + random.choice(self.settings['user']['mail']),
                'user_id': random.randint(208118596, 308118596)
            }

    def select_client(self):
        if not self.org:
            raise Exception("org should be initialized")

        curr_vyatta = random.randint(0, len(self.org.vyatta_list) - 1)
        self.vyatta = self.org.vyatta_list[curr_vyatta]
        self.curr_socket = random.choice(self.vyatta['sockets'])
        self.user_agent = random.choice(agent.user_agent_list)

