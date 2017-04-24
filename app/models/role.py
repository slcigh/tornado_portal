# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL


class Role(BaseModel):
    table = 'role_role'
    field_list = ['create_time', 'update_time',
                  'name', 'pinyin_name', 'introduce',
                  'avatar', 'imagery', 'back_img', 'banner',
                  'full_imagery', 'gender', 'role_type', 'camp_id',
                  'organize_id', 'race_type', 'profession']

    @classmethod
    @gen.coroutine
    def list(cls, role_type=None):
        query = u"""
        SELECT
           `role_role`.`id`,
           `role_role`.`name`,
            CASE `role_role`.`gender`
                WHEN 0 THEN '男'
                WHEN 1 THEN '女'
                WHEN 2 THEN '未知'
            END AS `gender`,
            CASE `role_role`.`role_type`
                WHEN  3 THEN '用户'
                ELSE '官方'
            END AS `role_type`,
            CASE `role_role`.`race_type`
                WHEN 0 THEN '普通人'
                WHEN 1 THEN '天选者'
                WHEN 2 THEN '守护者'
                WHEN 3 THEN '启蒙者'
                ELSE '未知'
            END AS 'race_type',
            CASE
                WHEN `auth_user`.`username` IS NULL
                  THEN '官方'
                ELSE `auth_user`.`username`
            END AS `owner`,
           `camp_camp`.`name` AS `camp`,
            CASE
                WHEN `organize_organize`.`name` IS NULL
                  THEN '无'
                ELSE `organize_organize`.`name`
            END AS `organize`,
            (SELECT COUNT(*)
             FROM `auth_user`
             INNER JOIN `role_role_follower`
             ON (`auth_user`.`id` = `role_role_follower`.`user_id`)
             WHERE `role_role_follower`.`role_id` = `role_role`.`id`)
             AS 'fans_count'
        FROM `role_role`
        LEFT OUTER JOIN `auth_user` ON (`role_role`.`owner_id` = `auth_user`.`id`)
        LEFT OUTER JOIN `camp_camp` ON (`role_role`.`camp_id` = `camp_camp`.`id`)
        LEFT OUTER JOIN `organize_organize` ON (`role_role`.`organize_id` = `organize_organize`.`id`)"""
        if role_type == "official":
            query += 'WHERE NOT (`role_role`.`role_type` = 3)'
        if role_type == "user":
            query += 'WHERE `role_role`.`role_type` = 3'
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())


class RolePopularTags(BaseModel):
    table = 'role_rolepopulartags'
    field_list = ['content']
