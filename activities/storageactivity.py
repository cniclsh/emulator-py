
import activity
from apps import file

class UserLogin(activity.Activity):

    def __init__(self, settings, http_session_id, time_range, user, app, activity_name, activity_setting):
        super(UserLogin, self).__init__(settings, time_range, user, app, activity_name, activity_setting)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(UserLogin, self).logging_activity()
        record['activity'] = 'user_login'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['http_sess_id'] = self.http_sess_id

        return record

class UploadFile(activity.Activity):
    def __init__(self, settings, http_session_id, time_range, user, app, activity_name, activity_setting):
        super(UploadFile, self).__init__(settings, time_range, user, app, activity_name, activity_setting)
        self.file = file.upload_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(UploadFile, self).logging_activity()
        record['activity'] = 'upload_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class DownloadFile(activity.Activity):
    def __init__(self, settings, http_session_id, time_range, user, app, activity_name, activity_setting):
        super(DownloadFile, self).__init__(settings, time_range, user, app, activity_name, activity_setting)
        self.file = file.download_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(DownloadFile, self).logging_activity()
        record['activity'] = 'download_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class ShareFile(activity.Activity):
    def __init__(self, settings, http_session_id, time_range, user, app, activity_name, activity_setting):
        super(ShareFile, self).__init__(settings, time_range, user, app, activity_name, activity_setting)
        self.file = file.share_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(ShareFile, self).logging_activity()
        record['activity'] = 'share_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class ViewFile(activity.Activity):
    def __init__(self, settings, http_session_id, time_range, user, app, activity_name, activity_setting):
        super(ViewFile, self).__init__(settings, time_range, user, app, activity_name, activity_setting)
        self.file = file.view_file(app)
        self.http_sess_id = http_session_id

    def logging_activity(self):
        record = super(ViewFile, self).logging_activity()
        record['activity'] = 'download_file'
        record['login'], record['user_id'] = tuple(self.user.app_user_info[self.app.name].values())
        record['http_sess_id'] = self.http_sess_id
        record = dict(record.items() + self.file.items())

        return record

class StorageActivity(object):
    activities = {'user_login': UserLogin,
                  'upload_file': UploadFile,
                  'download_file': DownloadFile,
                  'share_file': ShareFile,
                  'view_file': ViewFile}

    def __new__(kcls, settings, http_session_id, time_range, user, app, activity_name, activity_setting):

        return StorageActivity.activities[activity_name](settings, http_session_id, time_range, user, app, activity_name, activity_setting)


