# coding=utf-8
from tornado import gen
from app.model import POOL
from app.handlers.base import BaseHandler
from app.utils.oss import upload_image
from app.utils.other import current_time_string, name_to_pinyin


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
        name = self.get_argument('name')
        pinyin_name = name_to_pinyin(name)
        introduce = self.get_argument('introduce')
        gender = self.get_argument('gender')
        role_type = self.get_argument('role_type')
        camp_id = self.get_argument('camp_id')
        organize_id = self.get_argument('organize_id')
        race_type = self.get_argument('race_type')
        avatar = upload_image(self.request, 'avatar', prefix='role/avatar/', default='role/avatar/default.jpg')
        imagery = upload_image(self.request, 'imagery', prefix='role/imagery/', default='role/imagery/default.jpg')
        back_img = upload_image(self.request, 'back', prefix='role/back/', default='role/back/default.jpg')
        banner = upload_image(self.request, 'banner', prefix='role/banner/', default='role/banner/default.jpg')
        full_imagery = upload_image(self.request, 'full_imagery', prefix='role/full_imagery/')
        create_time = update_time = current_time_string()
        sql_express = """
        INSERT INTO `role_role`
        (`create_time`, `update_time`,`owner_id`,
        `name`, `pinyin_name`, `introduce`,
        `avatar`, `imagery`, `back_img`, `banner`,
        `full_imagery`,`gender`, `role_type`, `camp_id`,
        `organize_id`, `race_type`, `profession`)
        VALUES
        ('{}','{}',NULL,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','')""".format(create_time,
                                                                                                       update_time,
                                                                                                       name,
                                                                                                       pinyin_name,
                                                                                                       introduce,
                                                                                                       avatar, imagery,
                                                                                                       back_img, banner,
                                                                                                       full_imagery,
                                                                                                       gender,
                                                                                                       role_type,
                                                                                                       camp_id,
                                                                                                       organize_id,
                                                                                                       race_type)
        try:
            yield POOL.execute(sql_express)
            self.write({'status': 1})
        except Exception, e:
            print e
            self.write({'status': 0})
