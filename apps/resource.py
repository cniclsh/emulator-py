import boxfile
import file

class Resource(object):
    resources = {
                    "box" : boxfile.gen_predefined_resource,
                    "dropbox" : file.gen_predefined_resource,
                }

    def __init__(self, app_name):
        self.app_name = app_name
        self.predefined_resource = self._gen_predefined_resource()

    def _gen_predefined_resource(self):
        if self.app_name in Resource.resources:
            return Resource.resources[self.app_name]()
        return None
