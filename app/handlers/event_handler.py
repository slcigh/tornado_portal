# coding=utf-8
from tornado import gen
from app.models.event import Event, UserEvent, BugEvent
from app.handlers.base import BaseHandler
from app.utils.other import current_time_string, current_date_string
from app.utils.oss import upload_image


class EventHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        events = yield Event.list()
        self.write({"data": events})

    @gen.coroutine
    def delete(self, *args, **kwargs):
        eid = self.get_argument('rid', '')
        if eid:
            yield BugEvent.delete_by_query({"event_id": eid})
            yield UserEvent.delete_by_query({"event_id": eid})
            yield Event.delete_by_id(eid)
            self.write({"status": 1})
        else:
            self.write({"status": 0})

    @gen.coroutine
    def put(self, *args, **kwargs):
        op = self.get_argument('op')
        eid = self.get_argument('rid', '')
        if eid:
            if op == 'enable':
                yield Event.update({"use": 1}, eid)
            elif op == 'disable':
                yield Event.update({"use": 0}, eid)
            else:
                self.write({"status": 0})
        else:
            self.write({"status": 0})

    @gen.coroutine
    def post(self, *args, **kwargs):
        arg_dict = self.prepare_arg_dict()
        arg_dict['banner'] = upload_image(self.request, 'banner', prefix='event/banner/',
                                          default='event/banner/default.jpg')
        arg_dict['create_time'] = current_time_string()
        arg_dict['use'] = 1
        arg_dict['status'] = 1
        try:
            yield Event.create(arg_dict)
            self.write({"status": 1})
        except Exception, e:
            print e
            self.write({"status": 0})
