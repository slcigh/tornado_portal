# coding=utf-8
from tornado import gen
from app.models.post import Post, PostSet, PostDefaultCover
from app.handlers.base import BaseHandler


class PostDefaultCoverHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        datas = yield PostDefaultCover.list()
        self.write({"data": datas})


class PostHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        datas = yield Post.list()
        self.write({"data": datas})
