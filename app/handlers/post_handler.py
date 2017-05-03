# coding=utf-8
from tornado import gen
from app.models.post import Post, PostSet, PostDefaultCover
from app.handlers.base import BaseHandler


class PostDefaultCoverHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        data = yield PostDefaultCover.list()
        self.write({"data": data})


class PostHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        data = yield Post.list(role_type='user')
        self.write({"data": data})
