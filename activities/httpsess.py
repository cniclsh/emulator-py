import random
import string

import activity

from boxactivity import BoxActivity


PREDEFIND_ACTIVITY_LIST = {
    'box' : {
        "user_login": {
            "data_length": random.randint(1024, 2048)

        },
        "upload_file": {
            "data_length": random.randint(3096, 5120),
            "file": '',
            "parent": ''
        },
        "download_file": {
            "data_length": random.randint(3096, 5120),
            "file": '',
            "parent": ''
        },
        "share_file": {
            "data_length": random.randint(1024, 2048),
            "file": '',
            "parent": ''
        },
        "view_file": {
            "data_length": random.randint(3096, 5120),
            "file": '',
            "parent": ''
        },
    }
}


"""
    time_range: a workday, such as "2014-04-23"
"""
def emulate_http_sessions(settings, user, app, time_range):
    http_sess_list = []
    n_packet, n_activity = 0, 0
    n_http_sess = random.randint(settings['http-sess']['min'], settings['http-sess']['max'])
    sub_time_ranges = time_range.split(n_http_sess)
    for i in range(n_http_sess):
        http_sess = HttpSess(settings, user, app, sub_time_ranges[i])
        n_activity += http_sess.nactivity
        n_packet += http_sess.n_packet
        http_sess_list.append(http_sess.logging())

    return (n_packet, n_activity, http_sess_list)


"""
    HttpSess
    This class generates http traffic. There are 3 kinds of traffic:
    1. Noise: means traffic is unknown
    2. Light-way identified: means only app name is detected.
    3. Heavy-way identified: means user behaviors are detected.

"""
class HttpSess(object):
    deep_dive_apps = {'box': BoxActivity}

    def __init__(self, settings, user, app, time_range):
        self.settings = settings

        self.user = user
        user.select_socket()

        self.app = app
        app.select_socket()

        self.httpsess_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(26))

        activity_dict = PREDEFIND_ACTIVITY_LIST[app.name] if app.name in PREDEFIND_ACTIVITY_LIST else None

        self.nactivity = random.randint(settings['activity']['min'], settings['activity']['max'])

        self.time_ranges = time_range.split(self.nactivity)

        self.n_packet = 0

        self.activity_list = self._gen_activity_list(activity_dict)

    def _gen_activity_list(self, activity_dict):
        activities = []
        if not activity_dict:
            for i in range(self.nactivity):
                act = activity.Activity(self.time_ranges[i], self.user, self.app, 'unsupported')
                activities.append(act)
                self.n_packet += len(act.packet_list)
            return activities

        " The first activity should be 'user_login' "
        act = HttpSess.deep_dive_apps[self.app.name](self.httpsess_id,
                                                     self.time_ranges[0],
                                                     self.user, self.app,
                                                     'user_login',
                                                     activity_dict['user_login'])
        activities.append(act)
        self.n_packet += len(act.packet_list)

        new_activity_dict = {}
        for (k, v) in activity_dict.items():
            if k == 'user_login':
                continue

            new_activity_dict[k] = v

        activity_key_list = random.sample(new_activity_dict.keys() * (self.nactivity - 1),
                                          self.nactivity - 1)
        for activity_key in activity_key_list:

            act = HttpSess.deep_dive_apps[self.app.name](self.httpsess_id,
                                                         self.time_ranges[activity_key_list.index(activity_key)],
                                                         self.user, self.app,
                                                         activity_key, activity_dict[activity_key])
            activities.append(act)
            self.n_packet += len(act.packet_list)
        return activities

    def logging(self):
        logs = {'pkg':[], 'app':[]}

        for act in self.activity_list:
            logs['pkg'] += act.logging_tcpsess()

            if act.app.name in HttpSess.deep_dive_apps:
                logs['app'].append(act.logging_activity())

        return logs


