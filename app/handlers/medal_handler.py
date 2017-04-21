# coding=utf-8
from tornado import gen
from app.model import POOL
from app.handlers.base import BaseHandler


class MedalHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        sql_express = u"""
        SELECT
            `achievement_medal`.`id`,
            `achievement_medal`.`name`,
            `achievement_medal`.`image`,
            `achievement_medal`.`desc`,
            `achievement_medal`.`medal_type`,
            `achievement_medal`.`medal_num`,
            (SELECT COUNT(*) FROM `achievement_rolemedal`
            WHERE `achievement_rolemedal`.`medal_id` = `achievement_medal`.`id`) as `send_num`
        FROM `achievement_medal`"""
        cur = yield POOL.execute(sql_express)
        medals = cur.fetchall()
        self.write({"data": medals})
