import datetime
from pypinyin import lazy_pinyin


def current_time_string():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def current_date_string():
    return datetime.datetime.now().strftime('%Y-%m-%d')


def name_to_pinyin(name):
    return ''.join(lazy_pinyin(unicode(name)))
