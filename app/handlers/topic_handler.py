# coding=utf-8
from tornado import gen
from app.models.topic import Topic, TopicToday
from app.handlers.base import BaseHandler
from app.utils.other import current_time_string, current_date_string
from app.utils.oss import upload_image


class TopicHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        topics = yield Topic.list()
        self.write({"data": topics})

    @gen.coroutine
    def put(self, *args, **kwargs):
        op = self.get_argument('op', '')
        tid = self.get_argument('rid', '')
        try:
            if op == 'today':
                yield TopicToday.delete_all_today()
                arg_dict = {'create_time': current_time_string(), 'update_time': current_time_string(),
                            'topic_id': tid, 'date': current_date_string()}
                yield TopicToday.create(arg_dict)
            if op == 'rec':
                yield Topic.update({"is_recommend": 1}, tid)
            if op == 'rmrec':
                yield Topic.update({"is_recommend": 0}, tid)
            self.write({"status": 1})
        except Exception, e:
            print e
            self.write({"status": 0})

    @gen.coroutine
    def post(self, *args, **kwargs):
        arg_dict = self.prepare_arg_dict()
        title = arg_dict['title']
        arg_dict['title'] = u'#{}#'.format(title)
        arg_dict['cover'] = upload_image(self.request, 'cover', prefix='topic/cover/',
                                         default='topic/cover/default.jpg')
        arg_dict['create_time'] = current_time_string()
        arg_dict['update_time'] = current_time_string()
        arg_dict['is_recommend'] = 0
        try:
            yield Topic.create(arg_dict)
            self.write({"status": 1})
        except Exception, e:
            print e
            self.write({"status": 0})
