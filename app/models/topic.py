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


"""
        for t in TopicTempManager.objects.all().order_by('topic__pk'):
            if not t.topic.has_manager:
                tmp_dict = {'uid': t.user.id, 'tid': t.topic.id, 'topic_name': t.topic.title,
                            'username': t.user.username,
                            'user_home_url': '/user_center/#/{}'.format(t.user.userinfo.id)}
                result_list.append(tmp_dict)
        return json_response(result_list)
"""


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
        raise gen.Return(cursor.fetchall())
