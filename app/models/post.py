# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL
from app.utils.redis_util import add_hits_count


class PostDefaultCover(BaseModel):
    table = 'role_coverimagedefault'
    field_list = ['typename', 'image']


class PostSet(BaseModel):
    table = 'role_postset'
    field_list = ['create_time', 'update_time', 'title', 'introduce', 'cover_img', 'post_type', 'status', 'count',
                  'is_show', 'is_set', 'default_cover_id', 'role_id']


class Post(BaseModel):
    table = 'role_post'
    field_list = ['create_time', 'update_time', 'title', 'introduce', 'cover_img', 'post_type', 'index', 'name',
                  'content', 'tag_text', 'status', 'is_origin', 'is_show', 'default_cover_id', 'post_set_id',
                  'refer_to_id', 'role_id']

    @classmethod
    @gen.coroutine
    def list(cls, role_type=None):
        query = u"""
        SELECT
            `role_post`.`id`,
            `role_post`.`title`,
            `role_post`.`introduce`,
            `role_post`.`post_type`,
            DATE_FORMAT(`role_post`.`create_time`,'%Y-%m-%d') AS `create_time`,
            `role_post`.`content`,
            `role_role`.`id` AS `role_id`,
            `role_role`.`name` AS `role_name`
        FROM `role_post`
        INNER JOIN `role_role` ON (`role_post`.`role_id` = `role_role`.`id`)
        WHERE `role_post`.`is_show` = 1 {}
        ORDER BY `role_post`.`create_time` DESC"""
        if role_type == "official":
            query = query.format('AND NOT (`role_role`.`role_type` = 3)')
        if role_type == "user":
            query = query.format('AND `role_role`.`role_type` = 3')
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        data = list(map(add_hits_count, data))
        raise gen.Return(data)
