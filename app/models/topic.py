# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL
from app.utils.other import current_date_string


class Topic(BaseModel):
    table = 'topic_topic'
    field_list = ['create_time', 'update_time',
                  'title', 'desc', 'intro',
                  'is_recommend', 'cover']

    @classmethod
    @gen.coroutine
    def list(cls, role_type=None):
        query = u"""
            SELECT
                `topic_topic`.`id` AS `rid`,
                `topic_topic`.`title`,
                `topic_topic`.`intro`,
                IF(`topic_topic`.`is_recommend`,'是','否') as `is_recommend`,
                IF(
                  EXISTS(
                    SELECT 1
                      FROM `topic_topictoday`
                      WHERE (`topic_topictoday`.`topic_id` = `topic_topic`.`id`
                      AND `topic_topictoday`.`date` = '{current_date}')),'是','否') as `is_today`,
                (SELECT COUNT(*)
                FROM `topic_topicitem`
                WHERE `topic_topicitem`.`topic_id` = `topic_topic`.`id`) as 'item_count'
            FROM `topic_topic`""".format(current_date=current_date_string())
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)


class TopicToday(BaseModel):
    table = 'topic_topictoday'
    field_list = ['create_time', 'update_time', 'date', 'topic_id']

    @classmethod
    @gen.coroutine
    def delete_all_today(cls):
        query = u"""
        DELETE
        FROM `topic_topictoday`
        WHERE `topic_topictoday`.`date` = '{current_date}'""".format(current_date=current_date_string())
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())


class TopicManager(BaseModel):
    table = 'topic_topicmanager'
    field_list = ['create_time', 'update_time', 'user_id', 'topic_id']


class TopicTempManager(BaseModel):
    table = 'topic_topictempmanager'
    field_list = ['create_time', 'update_time', 'user_id', 'topic_id']

    @classmethod
    @gen.coroutine
    def list(cls):
        query = u"""
        SELECT
            `auth_user`.`id` AS `uid`,
            `auth_user`.`username` AS `username`,
            `topic_topic`.`id` AS `tid`,
            `topic_topic`.`title` AS `topic_name`
        FROM `topic_topictempmanager`
        INNER JOIN `topic_topic` ON (`topic_topictempmanager`.`topic_id` = `topic_topic`.`id`)
        LEFT OUTER JOIN `topic_topicmanager` ON (`topic_topic`.`id` = `topic_topicmanager`.`topic_id`)
        INNER JOIN `auth_user` ON (`topic_topictempmanager`.`user_id` = `auth_user`.`id`)
        WHERE `topic_topicmanager`.`id` IS NULL
        ORDER BY `topic_topictempmanager`.`topic_id` DESC"""
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)

    @classmethod
    @gen.coroutine
    def get_value_by_filter(cls, value_dict):
        query_get_id = u"""
        SELECT
            `auth_user`.`id` AS `user_id`,
        FROM `{table}`
        INNER JOIN `auth_user` ON (`topic_topictempmanager`.`user_id` = `auth_user`.`id`)
        WHERE ({values})""".format(table=cls.table, values=cls._parse_update_value_dict(value_dict))
        cursor = yield POOL.execute(query_get_id)
        data = cursor.fetchall()
        raise gen.Return(data)
