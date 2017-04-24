from tornado import gen
from . import POOL


class BaseModel(object):
    table = ''
    field_list = []

    @classmethod
    def _make_fields(cls):
        return u"({})".format(u",".join(map(lambda x: "`{}`".format(x), cls.field_list)))

    @classmethod
    def _make_values(cls):
        return u"({})".format(u",".join(map(lambda x: "'{" + x + "}'", cls.field_list)))

    @classmethod
    def _parse_update_value_dict(cls, value_dict):
        value_dict_str = u""
        for k, v in value_dict.items():
            value_dict_str += u"`{k}`='{v}',".format(k=k, v=v)
        return value_dict_str[:-1]

    @classmethod
    @gen.coroutine
    def list(cls):
        query = u"""
        SELECT *
        FROM `{table}`""".format(table=cls.table)
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())

    @classmethod
    @gen.coroutine
    def create(cls, field_dict):
        arg_dict = {'table': cls.table,
                    'fields': cls._make_fields(),
                    'values': cls._make_values()}
        query = u"""
        INSERT INTO `{table}` {fields}
        VALUES {values}""".format(**arg_dict).format(**field_dict)
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())

    @classmethod
    @gen.coroutine
    def update(cls, value_dict, mid):
        arg_dict = {'table': cls.table,
                    'id': mid,
                    'values': cls._parse_update_value_dict(value_dict)}

        query = u"""
        UPDATE `{table}`
        SET {values}
        WHERE `{table}`.`id` = {id}""".format(**arg_dict)
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())

    @classmethod
    @gen.coroutine
    def delete(cls, mid):
        arg_dict = {'table': cls.table,
                    'id': mid}
        query = u"""
        DELETE FROM `{table}`
        WHERE `{table}`.`id` = {id}""".format(**arg_dict)
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())
