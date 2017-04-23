# coding=utf-8
from tornado import gen
from app.models import POOL
from app.handlers.base import BaseHandler


class OrganizeNameIdListHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        sql_express = """
        SELECT
            `organize_organize`.`id`,
            `organize_organize`.`name`
        FROM `organize_organize`"""
        cur = yield POOL.execute(sql_express)
        organizies = cur.fetchall()
        self.write({"data": organizies})
