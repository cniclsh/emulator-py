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


def download_file(app):
    file = random.choice(app.resource.predefined_resource['files'].values())
    return file.get_brief_info()

def upload_file(app):
    file = File()
    app.resource.predefined_resource['files'][file.name] = file

    return file.get_brief_info()

def share_file(app):
    file = random.choice(app.resource.predefined_resource['files'].values())

    return file.get_brief_info()

def view_file(app):
    file = random.choice(app.resource.predefined_resource['files'].values())
    return file.get_brief_info()

def gen_predefined_resource():
    files = emulate_file_list(10)
    root = {
        "id": 0,
        "name": "All Files"
    }
    return {"folders": [root], "files": files}



BASE_TIMESTATMP = datetime.datetime(2013, 7, 21, 3, 13, 22, 259901)

FILE_TEMPLATE = {
        "id": 15136383736,
        "content_type": "image/jpeg",
        "created_by": "Andy Li",
        "created_by_user_id": 208118596,
        "name": "Water lilies.jpg",
        "parent": 1460450769,
        "parent_name": "Ebooks",
        "raw_size": 83794,
        "date": 1394430118,
        "deleted": 1394437676,
        "deleted_by": "null",
        "deleted_by_user_id": "null",
}

def emulate_file_list(nfile=1):
    files = {}
    for i in range(0, nfile):
        file = File(FILE_TEMPLATE)
        files[file.name] = file

    return files

class File(object):
    def __init__(self, template=FILE_TEMPLATE):
        """Convert a dictionary to a class

        @param :template Dictionary
        """
        self.__dict__.update(template)

        self.id, self.name, self.content_type, self.raw_size, self.date = self._gen_file_info()
        self.deleted, self.deleted_by, self.deleted_by_user_id = self._gen_deleted_info()
        self.created_by = self._gen_created_by()

    def _gen_file_info(self):
        file_id = random.randint(11111111111, 99999999999)
        name = str(file_id) + '.docx'
        content_type = random.choice([""] * 8 + ["image/jpeg", "image/gif", "text/csv", "video/mpeg"])
        size = random.randint(1, 10000000)
        create_time = time.mktime(BASE_TIMESTATMP.timetuple()) + random.randint(0, 100000)

        return file_id, name, content_type, size, create_time

    def _gen_created_by(self):
        return ""

    def _gen_deleted_info(self):
        return 0, 'null', 'null'

    def get_brief_info(self):
        return {
            'file_name': self.name,
            'file_type': self.content_type if self.content_type != '' else 'unknown',
            'file_size': self.raw_size
        }




