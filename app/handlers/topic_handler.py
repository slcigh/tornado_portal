# coding=utf-8
from tornado import gen
from app.models.topic import Topic, TopicToday, TopicManager, TopicTempManager
from app.models.message import Announce, UserAnnounce
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


class TopicTempManagerHandler(BaseHandler):
    @gen.coroutine
    def get(self, *args, **kwargs):
        data = yield TopicTempManager.list()
        self.write({"data": data})

    @gen.coroutine
    def post(self, *args, **kwargs):
        uid = self.get_argument('uid', '')
        tid = self.get_argument('tid', '')
        if not uid or not tid:
            self.write({"status": 0})
        else:
            topic_manager_arg_dict = {'user_id': uid, 'topic_id': tid, 'create_time': current_time_string(),
                                      'update_time': current_time_string()}
            yield TopicManager.create(topic_manager_arg_dict)
            yield Announce.create_if_not_exist(
                {"title": u"话题管理员申请通知", 'create_time': current_time_string(), 'content': '', 'url': ''})
            announce_id = yield Announce.get_id_by_filter({"title": u"话题管理员申请通知"})
            user_announce_success_arg_dict = {'user_id': uid, 'announce_id': announce_id, 'read': 0,
                                              'content': u'恭喜你，话题管理员申请通过'}
            yield UserAnnounce.create(user_announce_success_arg_dict)
            values = yield TopicTempManager.get_value_by_filter({"topic_id": tid})
            for i in values:
                user_id = i['user_id']
                user_announce_fail_arg_dict = {'user_id': user_id, 'announce_id': announce_id, 'read': 0,
                                               'content': u'话题管理员申请失败'}
                yield UserAnnounce.create(user_announce_fail_arg_dict)
            yield TopicTempManager.delete(tid)
            """
            try:
                sttm = TopicTempManager.objects.filter(topic=topic, user=user).first()
                sttm.delete()
                ann = Announce.objects.get_or_create(title=u'话题管理员申请通知')[0]
                UserAnnounce.objects.create(user=user, announce=ann, content=u'恭喜你，话题管理员申请通过')
                for ttm in t:
                    UserAnnounce.objects.create(user=ttm.user, announce=ann, content=u'话题管理员申请失败')
                    ttm.delete()
            except:
                pass
            if user not in topic.follower.all():
                topic.follower.add(user)
                topic.save()
            """
            self.write({"status": 1})
