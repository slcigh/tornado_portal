# coding=utf-8
from tornado import gen
from app.models import POOL
from app.handlers.base import BaseHandler


class UserHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        sql_express = u"""
        SELECT COUNT(*) as `user_count`
        FROM `account_userinfo`
        WHERE TIMESTAMPDIFF(SECOND, last_visit, now()) < 600;"""
        cur = yield POOL.execute(sql_express)
        try:
            online_users = cur.fetchone()['user_count']
        except Exception, e:
            print e
            online_users = 0
        sql_express = u"""
        SELECT
            `auth_user`.`username`,
            `account_userinfo`.`last_visit`,
            IF(`account_userinfo`.`mobile` = '','未绑定',`account_userinfo`.`mobile`) as `mobile`,
            IF(`auth_user`.`is_active`,'正常','冻结') AS `freeze`,
            IF(`account_userinfo`.`email` = '','未绑定',`account_userinfo`.`email`) as `email`,
            `account_userinfo`.`nickname`,
            `auth_user`.`id`,
            `auth_user`.`date_joined` AS `date_joined`
        FROM `account_userinfo`
        INNER JOIN `auth_user` ON (`account_userinfo`.`user_id` = `auth_user`.`id`)
        WHERE NOT (`auth_user`.`is_staff` = 1)"""
        cur = yield POOL.execute(sql_express)
        userinfo = cur.fetchall()
        self.write({"online_users": online_users, "users_info": userinfo})
