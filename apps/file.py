"""

"file_15136383736": {
    "id": 15136383736
    "comments_count": "0",
    "content_type": "image/jpeg",
    "created_by": "Andy Li",
    "created_by_user_id": 208118596,
    "downloadable": true,
    "name": "Water lilies.jpg",
    "owner": "Andy Li",
    "owner_disabled_shared_download": false,
    "parent": 1460450769,
    "parent_name": "Ebooks",
    "raw_size": 83794,
    "date": 1394430118,
    "deleted": 1394437676,
    "deleted_by": "Andy Li",
    "deleted_by_user_id": 208118596,
    "deleted_from_trash": 1397029676,
    "shared": true,
    "shared_access": 0,
    "shared_access_levels": {
                "0": true,
                "1": true,
                "2": true
    },
    "shared_link": "https://stratusee1.box.com/s/0089s1swvf2k1plz46ki",
    "has_password": null,
    "shared_download_count": 1,
    "shared_download_off": null
}

"""
import random
import datetime
import time

BASE_TIMESTATMP = datetime.datetime(2013, 7, 21, 3, 13, 22, 259901)

FILE_TEMPLATE = {
        "id": 15136383736,
        "comments_count": "0",
        "content_type": "image/jpeg",
        "created_by": "Andy Li",
        "created_by_user_id": 208118596,
        "downloadable": True,
        "name": "Water lilies.jpg",
        "owner": "Andy Li",
        "owner_disabled_shared_download": False,
        "parent": 1460450769,
        "parent_name": "Ebooks",
        "raw_size": 83794,
        "date": 1394430118,
        "deleted": 1394437676,
        "deleted_by": "null",
        "deleted_by_user_id": "null",
        "shared": True,
        "shared_access": 0,
        "shared_access_levels": {
                    "0": True,
                    "1": True,
                    "2": True
        },
        "shared_link": "https://stratusee1.box.com/s/0089s1swvf2k1plz46ki",
        "has_password": "null",
        "shared_download_count": 1,
        "shared_download_off": 'null'
}

def emulate_file_list(nfile=1):
    files = {}
    for i in range(0, nfile):
        file = File(FILE_TEMPLATE)
        files[file.name] = file

    return files


class SharedAccessLevel(object):
    def __init__(self, levels):
        self.__dict__.update(levels)

    def _gen_shared_info(self):
        shared = random.choice([True, True, True, False, False])
        if shared:
            shared_access = random.randint(0, 10)
            shared_access_levels = {
                "0": random.choice([True, True, True, True, False]),
                "1": random.choice([True, True, True, False, False]),
                "2": random.choice([True, True, False, False, False])
            }

            shared_link = "https://stratusee1.box.com/s/0089s1swvf2k1plz46ki"
            has_password = "null"
            shared_download_count =  random.randint(0, 10)
            shared_download_off = 'null'

            return shared, shared_access, shared_access_levels, shared_link, has_password, shared_download_count, shared_download_off

        else:
            return shared, 'null', 'null', 'null', 'null', 'null', 'null'


class File(object):
    def __init__(self, template):
        """Convert a dictionary to a class

        @param :template Dictionary
        """
        self.__dict__.update(template)
        for k, v in template.items():
            if k == 'shared_access_levels':
                self.__dict__[k] = SharedAccessLevel(v)

        self.id, self.name, self.content_type, self.raw_size, self.date = self._gen_file_info()
        self.comments_count = self._gen_comments_info()
        self.owner_disabled_shared_download = self._gen_owner_disabled_shared_download()
        self.deleted, self.deleted_by, self.deleted_by_user_id = self._gen_deleted_info()
        self.created_by = self._gen_created_by()

        self.shared, self.shared_access, self.shared_access_levels,\
            self.shared_link, self.has_password, self.shared_download_count, \
            self.shared_download_off = self.shared_access_levels._gen_shared_info()


    def _gen_file_info(self):
        file_id = random.randint(11111111111, 99999999999)
        name = str(file_id) + '.docx'
        content_type = random.choice([""] * 8 + ["image/jpeg", "image/gif", "text/csv", "video/mpeg"])
        size = random.randint(1, 10000000)
        create_time = time.mktime(BASE_TIMESTATMP.timetuple()) + random.randint(0, 100000)

        return file_id, name, content_type, size, create_time

    def _gen_comments_info(self):
        return random.randint(0, 100)

    def _gen_created_by(self):
        return ""

    def _gen_owner_disabled_shared_download(self):
        options = [False] * 9 + [True]
        return random.choice(options)

    def _gen_deleted_info(self):
        return 0, 'null', 'null'


if __name__ == '__main__':
    file = emulate_file_list(3)

    print file




