# coding=utf-8
from app.models.base import BaseModel
from tornado import gen
from . import POOL
# from app.utils.redis_util import add_hits_count


class PostDefaultCover(BaseModel):
    table = 'role_coverimagedefault'
    field_list = ['typename', 'image']


class PostSet(BaseModel):
    table = 'role_postset'
    field_list = ['create_time', 'update_time', 'title', 'introduce', 'cover_img', 'post_type', 'status', 'count',
                  'is_show', 'is_set', 'default_cover_id', 'role_id']


"""
   {
        "role": {
            "id": 182,
            "name": "玄素"
        },
        "id": 300,
        "title": "玄素_人物设定",
        "introduce": "诞生于宋朝并且最终修炼有成晋升了五维的蛇妖，因为在修炼过程中受过道士的欺负，所以即使到了五维也总想找道士报仇。被武先生召唤后本想进行自己的复仇大业，但是很快被现代五光十色的世界所吸引，把复仇什么的丢到了脑后。",
        "post_type": 0,
        "create_time": "2017-02-24 10:53:34",
        "extra_info": {
            "content": "<p>                        属性设定：<br>身份：守护者 召唤者武先生<br>所属：夺灵者 灵蛇组<br>职业：大妖<br>性别：女<br>年龄：735<br>星座：水瓶<br>血型：AB<br>喜好：烤田鸡，漂亮的衣服，自己手工制作各种簪子。<br>性格：活泼开朗，无忧无虑。<br>座右铭或口头禅：啊啊啊，老武救命啊，这月信用卡又超支啦。<br>一句话定义：看起来很高傲其实很呆萌的大姐姐。</p><p>形象设定：<br>身高：174<br>肤色：偏白<br>发色：黑色<br>装束喜好：黑色长裙，深色系的汉风古装。<br>外貌：黑色笔直的长发，如果不笑就是气质高冷的大姐姐，但是一笑会露出虎牙，气质瞬间变得呆萌。<br>标志物：用自己褪掉的皮做的蛇皮手袋，经常拿来送礼……</p><p>背景设定：<br>诞生于宋朝并且最终修炼有成晋升了五维的蛇妖，因为在修炼过程中受过道士的欺负，所以即使到了五维也总想找道士报仇。被武先生召唤后本想进行自己的复仇大业，但是很快被现代五光十色的世界所吸引，把复仇什么的丢到了脑后。<br>虽然已经活了好几百年，但是本质上还是非常单纯，总想装得成熟但是总是露馅。她的快乐开朗是武先生充满杀戮的生活中最后的救赎，与其说她是守护者，倒不如说是武先生一直在守护着无忧无虑的她。<br>善于用毒，最强的毒素几乎无人可解。人形时不擅战斗，只会使用些无关痛痒的小法术，但是一旦恢复原形，则战力暴增，不过非常不喜欢在武先生面前显露原形。<br>第一级能力——原始之毒：黑蛇的本命毒素，能够产生催眠、混乱、死亡等多种负面效果，几乎无药可救。<br>第二级能力——蛇瞳：当此能力发动时，所有与其对视的生物都有可能陷入恐慌，此几率视生物的意志力而定。<br></p>",
            "hits_count": 4
        }
    },
"""


class Post(BaseModel):
    table = 'role_post'
    field_list = ['create_time', 'update_time', 'title', 'introduce', 'cover_img', 'post_type', 'index', 'name',
                  'content', 'tag_text', 'status', 'is_origin', 'is_show', 'default_cover_id', 'post_set_id',
                  'refer_to_id', 'role_id']

    @classmethod
    @gen.coroutine
    def list(cls):
        query = u"""
        SELECT
            `role_post`.`id`,
            `role_post`.`title`,
            `role_post`.`introduce`,
            `role_post`.`post_type`,
            DATE_FORMAT(`role_post`.`create_time`,'%Y-%m-%d') AS `create_time`,
            `role_post`.`content`,
            `role_role`.`id` AS `role_id`,
            `role_role`.`name` AS `role_name`
        FROM `role_post`
        INNER JOIN `role_role` ON (`role_post`.`role_id` = `role_role`.`id`)
        WHERE `role_post`.`is_show` = 1
        ORDER BY `role_post`.`create_time` DESC"""
        cursor = yield POOL.execute(query)
        data = cursor.fetchall()
        # data = list(map(add_hits_count, data))
        raise gen.Return(data)
