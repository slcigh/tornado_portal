# coding=utf-8
import redis
from config import REDIS_HOST, REDIS_PORT, REDIS_PWD, REDIS_DB

POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PWD, db=REDIS_DB)


def get_server():
    my_server = redis.Redis(connection_pool=POOL)
    return my_server


def keys(qs):
    my_server = redis.Redis(connection_pool=POOL)
    return my_server.keys(qs)


def r_expire(key, seconds):
    my_server = redis.Redis(connection_pool=POOL)
    return my_server.expire(key, seconds)


def get_value(value):
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.get(value)
    return response


def set_value(key, value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.set(key, value)


def r_push(key, value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.rpush(key, value)


def l_push(key, value):
    my_server = redis.Redis(connection_pool=POOL)
    my_server.lpush(key, value)


def l_range(key, start=None, end=None):
    if start is None:
        start = 0
    if end is None:
        end = -1
    my_server = redis.Redis(connection_pool=POOL)
    response = my_server.lrange(key, start, end)
    return response


def l_rem(name, value, num=None):
    my_server = redis.Redis(connection_pool=POOL)
    if num is None:
        num = 0
    response = my_server.lrem(name, value, num)
    return response


def incr(name, num=None):
    my_server = redis.Redis(connection_pool=POOL)
    if num is None:
        num = 1
    response = my_server.incr(name, amount=num)
    return response


# 作品点击数
def get_hits_count(pid):
    name = "pv{}".format(pid)
    try:
        return int(get_value(name))
    except:
        return 0


# 话题点击数
def get_topic_hits_count(tid):
    name = "thits{}".format(tid)
    try:
        return int(get_value(name))
    except:
        return 0


# 话题总点击数
def get_topic_total_hits_count():
    try:
        return sum([int(get_value(key)) for key in keys("thits*")])
    except:
        return 1


# 设置expire
def check_or_set_expire(key, seconds):
    if not r_expire(key, seconds):
        r_expire(key, seconds)


def add_hits_count(post_dict):
    try:
        hits_count = get_hits_count(post_dict['id'])
    except:
        hits_count = 0
    post_dict['hits_count'] = hits_count
    return post_dict
