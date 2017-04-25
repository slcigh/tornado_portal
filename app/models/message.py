# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL


class Announce(BaseModel):
    table = 'account_announce'
    field_list = ['url', 'title',
                  'content', 'create_time']


class UserAnnounce(BaseModel):
    table = 'account_userannounce'
    field_list = ['user_id', 'announce_id',
                  'read', 'content']
