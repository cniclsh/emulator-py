import time
from datetime import datetime
import random
from itertools import izip, tee


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)


class TimeRange(object):
    def __init__(self, day_begin, day_end, format='str'):
        if format == 'str':
            self.begin = int(time.mktime(datetime.strptime(day_begin + ' 08:00:00', '%Y-%m-%d %H:%M:%S').timetuple()))
            self.end = int(time.mktime(datetime.strptime(day_end + ' 18:00:00', '%Y-%m-%d %H:%M:%S').timetuple()))
        else:
            self.begin = day_begin
            self.end = day_end

    def __getattr__(self, item):
        if item == 'str_begin':
            return datetime.fromtimestamp(self.begin).strftime("%Y-%m-%dT%H:%M:%S")
        elif item == 'str_end':
            return datetime.fromtimestamp(self.end).strftime("%Y-%m-%dT%H:%M:%S")
        else:
            raise Exception("Wrong attribute")

    def get_points(self, npoint=1):
        result = []
        collection = range(self.begin, self.end + 1)
        if len(collection) < npoint:
            collection *= npoint

        sorted = random.sample(collection, npoint)
        sorted.sort()
        for timestamp in sorted:
            result.append(datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H:%M:%S"))

        return result

    """
        split
        This function return 'nsplit' TimeRange objects
    """
    def split(self, nsplit=2):
        if nsplit in [0, 1]:
            return self

        result = []
        collection = range(self.begin, self.end)
        if not collection:
            collection = [self.begin] * (nsplit-1)
        elif len(collection) < nsplit-1:
            collection *= nsplit-1

        collection = random.sample(collection, nsplit-1) + [self.begin, self.end]
        collection.sort()

        for begin, end in pairwise(collection):
            result.append(TimeRange(begin, end, 'timestamp'))

        return result
