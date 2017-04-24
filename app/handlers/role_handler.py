# coding=utf-8
from tornado import gen
from app.models.role import Role, RolePopularTags
from app.handlers.base import BaseHandler
from app.utils.oss import upload_image
from app.utils.other import current_time_string, name_to_pinyin


class RoleHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        role_type = self.get_argument("type", None)
        roles = yield Role.list(role_type=role_type)
        self.write({"data": roles})

    @gen.coroutine
    def post(self, *args, **kwargs):
        arg_dict = self.prepare_arg_dict()
        name = self.get_argument('name')
        pinyin_name = name_to_pinyin(name)
        arg_dict['pinyin_name'] = pinyin_name
        arg_dict['avatar'] = upload_image(self.request, 'avatar', prefix='role/avatar/',
                                          default='role/avatar/default.jpg')
        arg_dict['imagery'] = upload_image(self.request, 'imagery', prefix='role/imagery/',
                                           default='role/imagery/default.jpg')
        arg_dict['back_img'] = upload_image(self.request, 'back', prefix='role/back/', default='role/back/default.jpg')
        arg_dict['banner'] = upload_image(self.request, 'banner', prefix='role/banner/',
                                          default='role/banner/default.jpg')
        arg_dict['full_imagery'] = upload_image(self.request, 'full_imagery', prefix='role/full_imagery/')
        arg_dict['create_time'] = current_time_string()
        arg_dict['update_time'] = current_time_string()
        arg_dict['profession'] = ''
        try:
            yield Role.create(arg_dict)
            self.write({'status': 1})
        except Exception, e:
            print e
            self.write({'status': 0})


class RoleTagHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        tags = yield RolePopularTags.list()
        self.write({"data": tags})

    @gen.coroutine
    def post(self, *args, **kwargs):
        op = self.get_argument('op', '')
        tid = self.get_argument('rid', '')
        content = self.get_argument('content', '')
        arg_dict = {"content": content}
        if op == 'del' and tid:
            yield RolePopularTags.delete(tid)
        elif content:
            yield RolePopularTags.create(arg_dict)
        self.write({'status': 1})
