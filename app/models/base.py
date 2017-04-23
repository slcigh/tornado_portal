from tornado import gen
from . import POOL


class BaseModel(object):
    table = ''
    field_list = []

    @classmethod
    def _make_fields(cls):
        return u"({})".format(u",".join(map(lambda x: "`{}`".format(x), cls.field_list)))

    @classmethod
    def _make_vales(cls):
        return u"({})".format(u",".join(map(lambda x: "'{" + x + "}'", cls.field_list)))

    @classmethod
    @gen.coroutine
    def create(cls, field_dict):
        arg_dict = {'table': cls.table,
                    'fields': cls._make_fields(),
                    'values': cls._make_vales()}
        query = u"""
        INSERT INTO `{table}` {fields}
        VALUES {values}""".format(**arg_dict).format(**field_dict)
        cursor = yield POOL.execute(query)
        raise gen.Return(cursor.fetchall())
