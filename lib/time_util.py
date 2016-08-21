import datetime
import time

formatStr = '%Y-%m-%d %H:%M:%S.%f'

def str_datetime(data_str):
    if data_str == None:
        return None
    return datetime.datetime.strptime(str(data_str), formatStr)

def datetime_str(ddate):
    if ddate == None:
        return None
    return ddate.strftime(formatStr)


def get_timestamp(this_time):
    return time.mktime(datetime.datetime.strptime(this_time, formatStr).timetuple())
def get_date(timestamp):
    return datetime.datetime.fromtimestamp(timestamp).strftime(formatStr)


