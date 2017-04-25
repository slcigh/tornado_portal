from tornado import gen
from . import POOL


class BaseModel(object):
    table = ''
    field_list = []

    @classmethod
    def _make_fields(cls):
        """
        :return:
            u'(`create_time`,`update_time`,`title`,`desc`,`intro`,`is_recommend`,`cover`)'
        """
        return u"({})".format(u",".join(map(lambda x: "`{}`".format(x), cls.field_list)))

    @classmethod
    def _make_values(cls):
        """
        :return:
            u"('{create_time}','{update_time}','{title}','{desc}','{intro}','{is_recommend}','{cover}')"
        """
        return u"({})".format(u",".join(map(lambda x: "'{" + x + "}'", cls.field_list)))

    @classmethod
    def _parse_where_value_dict(cls, value_dict):
        """
        :param value_dict: {'k1':'v1','k2':'v2'}
        :return:
            u"`k1`='v1' AND `k2`='v2'"
        """
        value_dict_str = u""
        for k, v in value_dict:
            value_dict_str += u"`{k}`='{v}' AND ".format(k=k, v=v)
        return value_dict_str.rstrip(u'AND')

    @classmethod
    def _parse_update_value_dict(cls, value_dict):
        """
        :param value_dict:
        :return:
            u"`name`='asdf123',`age`='12'"
        """
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
        data = cursor.fetchall()
        raise gen.Return(data)

    @classmethod
    @gen.coroutine
    def create(cls, field_dict):
        arg_dict = {'table': cls.table,
                    'fields': cls._make_fields(),
                    'values': cls._make_values()}
        print arg_dict
        query = u"""
        INSERT INTO `{table}` {fields}
        VALUES {values}""".format(**arg_dict).format(**field_dict)
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)

    @classmethod
    @gen.coroutine
    def create_if_not_exist(cls, field_dict):
        arg_dict = {'table': cls.table,
                    'fields': cls._make_fields(),
                    'x_values': cls._make_values()[1:-1],
                    'and_values': cls._parse_where_value_dict(field_dict)}
        query = u"""
        INSERT INTO INSERT INTO `{table}` {fields}
        SELECT
             {x_values}
        FROM DUAL
        WHERE NOT EXISTS (
          SELECT 1
          FROM `{table}`
          WHERE
            {and_values}
          LIMIT 1)""".format(**arg_dict).format(**field_dict)
        print query
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)

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
        data = cursor.fetchall()
        raise gen.Return(data)

    @classmethod
    @gen.coroutine
    def delete(cls, mid):
        arg_dict = {'table': cls.table,
                    'id': mid}
        query = u"""
        DELETE FROM `{table}`
        WHERE `{table}`.`id` = {id}""".format(**arg_dict)
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        raise gen.Return(data)

    @classmethod
    @gen.coroutine
    def get_id_by_filter(cls, value_dict):
        query_get_id = u"""
        SELECT `{table}`.`id`
        FROM `{table}`
        WHERE ({values}) LIMIT 1""".format(table=cls.table, values=cls._parse_update_value_dict(value_dict))
        cursor = yield POOL.execute(query_get_id)
        data = cursor.fetchone()
        raise gen.Return(data['id'])

    @classmethod
    @gen.coroutine
    def get_ids_by_filter(cls, value_dict):
        query_get_id = u"""
        SELECT `{table}`.`id`
        FROM `{table}`
        WHERE ({values})""".format(table=cls.table, values=cls._parse_update_value_dict(value_dict))
        cursor = yield POOL.execute(query_get_id)
        data = cursor.fetchall()
        raise gen.Return(data)
