# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL


class Event(BaseModel):
    table = 'base_event'
    field_list = ['create_time', 'start_time', 'expire_time',
                  'title', 'url', 'intro', 'banner',
                  'status', 'use']

    @classmethod
    @gen.coroutine
    def list(cls, role_type=None):
        query = u"""
        SELECT
            `base_event`.`id` AS `rid`,
            CASE `base_event`.`use`
              WHEN 0 THEN '否'
              WHEN 1 THEN '是'
            END AS 'use',
            `base_event`.`title`,
            `base_event`.`url`,
            DATE_FORMAT(`base_event`.`expire_time`,'%Y-%m-%d') AS `expire_time`,
            DATE_FORMAT(`base_event`.`start_time`,'%Y-%m-%d') AS `start_time`
        FROM `base_event`"""
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)


class UserEvent(BaseModel):
    table = 'base_userevent'
    field_list = ['create_time', 'user_id', 'event_id']


class BugEvent(BaseModel):
    table = 'base_bugevent'
    field_list = ['create_time', 'event_id', 'user_type',
                  'content', 'user_id', 'nickname', 'contact']
