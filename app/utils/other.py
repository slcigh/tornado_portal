import datetime


def current_time_string():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
