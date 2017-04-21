# coding=utf-8
from tornado import gen
from app.model import POOL
from app.handlers.base import BaseHandler


class TaskRecordHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        sql_express = u"""
        SELECT `role_role`.`id` as `rid`,
        `role_role`.`name` as `role_name`,
        `role_roleinfo`.`level` as `role_level`,
        `role_roleinfo`.`exp` as `role_exp`,
        (SELECT COUNT(*) FROM `task_roletaskpool`
        WHERE (`task_roletaskpool`.`role_id` = `role_role`.`id`
        AND `task_roletaskpool`.`status` = 2)) as `finished_task_count`
        FROM `role_role`
        LEFT OUTER JOIN `role_roleinfo` ON (`role_role`.`id` = `role_roleinfo`.`role_id`)
        WHERE `role_role`.`role_type` = 3"""
        cur = yield POOL.execute(sql_express)
        tasks = cur.fetchall()
        self.write({"data": tasks})
