import activity
from apps import boxfile


class UserLogin(activity.Activity):

    def __init__(self, http_session_id, time_range, user, app, activity_name, activity_value):
        super(UserLogin, self).__init__(time_range, user, app, activity_name, activity_value['data_length'])
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(UserLogin, self).logging_activity()
        record['activity'] = 'user_login'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['success'] = True
        record['http_sess_id'] = self.http_sess_id

        return record

class UploadFile(activity.Activity):
    def __init__(self, http_session_id, time_range, user, app, activity_name, activity_value):
        super(UploadFile, self).__init__(time_range, user, app, activity_name, activity_value['data_length'])
        self.file = boxfile.upload_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(UploadFile, self).logging_activity()
        record['activity'] = 'upload_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['success'] = True
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class DownloadFile(activity.Activity):
    def __init__(self, http_session_id, time_range, user, app, activity_name, activity_value):
        super(DownloadFile, self).__init__(time_range, user, app, activity_name, activity_value['data_length'])
        self.file = boxfile.download_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(DownloadFile, self).logging_activity()
        record['activity'] = 'download_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['success'] = True
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class ShareFile(activity.Activity):
    def __init__(self, http_session_id, time_range, user, app, activity_name, activity_value):
        super(ShareFile, self).__init__(time_range, user, app, activity_name, activity_value['data_length'])
        self.file = boxfile.share_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(ShareFile, self).logging_activity()
        record['activity'] = 'share_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['success'] = True
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class ViewFile(activity.Activity):
    def __init__(self, http_session_id, time_range, user, app, activity_name, activity_value):
        super(ViewFile, self).__init__(time_range, user, app, activity_name, activity_value['data_length'])
        self.file = boxfile.view_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(ViewFile, self).logging_activity()
        record['activity'] = 'download_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['success'] = True
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class BoxActivity(object):
    activities = {'user_login': UserLogin,
                  'upload_file': UploadFile,
                  'download_file': DownloadFile,
                  'share_file': ShareFile,
                  'view_file': ViewFile}

    def __new__(kcls, http_session_id, time_range, user, app, activity_name, data_length):
        return BoxActivity.activities[activity_name](http_session_id, time_range, user, app, activity_name, data_length)



