# coding=utf-8
from tornado import gen, escape
from app.model import POOL
from app.handlers.base import BaseHandler
from app.utils.oss import upload_image
from app.utils.other import current_time_string


class RoleHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        role_type = self.get_argument("type", None)
        sql_express = """
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
            sql_express += 'WHERE NOT (`role_role`.`role_type` = 3)'
        if role_type == "user":
            sql_express += 'WHERE `role_role`.`role_type` = 3'
        cur = yield POOL.execute(sql_express)
        roles = cur.fetchall()
        self.write({"data": roles})

    @gen.coroutine
    def post(self, *args, **kwargs):
        name = upload_image(self.request, 'imagery', 'role/avatar/')
        current_time = current_time_string()
        sql_express = """
        INSERT INTO `role_role`
        (`create_time`, `update_time`,`owner_id`,
        `name`, `pinyin_name`, `introduce`,
        `avatar`, `imagery`, `back_img`, `banner`,
        `full_imagery`,`gender`, `role_type`, `camp_id`,
        `organize_id`, `race_type`, `profession`)
        VALUES
        ({},{},NULL,
        'test34',
        'test34',
        '这家伙很懒，什么都没有留下!',
        'sdf.jpg',
        'role/imagery/default_female.jpg',
        'role/back/default.jpg',
        'role/banner/default.jpg',
        '',
        1,
        3,
        3,
        58,
        0,
        '')
        """.format(current_time, current_time)
        self.write({'roles': "ok"})
