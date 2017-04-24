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
        raise gen.Return(cursor.fetchall())


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
