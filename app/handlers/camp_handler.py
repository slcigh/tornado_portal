# coding=utf-8
from tornado import gen
from app.models import POOL
from app.handlers.base import BaseHandler


class CampNameIdListHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        sql_express = """
        SELECT
            `camp_camp`.`id`,
            `camp_camp`.`name`
        FROM `camp_camp`"""
        cur = yield POOL.execute(sql_express)
        camps = cur.fetchall()
        self.write({"data": camps})
