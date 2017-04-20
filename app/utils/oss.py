# coding=utf-8
import oss2
from uuid import uuid4
from config import ACCESS_KEY_ID, ACCESS_KEY_SECRET, BUCKET_NAME, END_POINT


def get_bucket():
    try:
        auth = oss2.Auth(ACCESS_KEY_ID, ACCESS_KEY_SECRET)
        bucket = oss2.Bucket(auth, END_POINT, BUCKET_NAME)
    except:
        bucket = None
    return bucket


def uuid_filename(filename):
    ext = filename.split('.')[-1]
    return '{}.{}'.format(uuid4().hex, ext)


def upload_image(request, name, prefix=None):
    try:
        t_file = request.files[name][0]
        original_filename = t_file['filename']
        filename = uuid_filename(original_filename)
        if prefix:
            filename = prefix + filename
        filedata = t_file['body']
        bucket = get_bucket()
        bucket.put_object(filename, filedata)
        return filename
    except:
        return None
