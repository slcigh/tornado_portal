import os
import uuid
import json
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def prepare_json(self, data):
        if isinstance(data, dict):
            items = data.items()
        else:
            items = enumerate(data)
        for k, v in items:
            if isinstance(v, dict) or isinstance(v, list):
                data[k] = self.prepare_json(v)
            else:
                try:
                    json.dumps(v)
                except (TypeError, OverflowError, ValueError):
                    data[k] = str(v)
        return data

    def write(self, response):
        data = self.prepare_json(response)
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Credentials", "true")
        self.set_header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE")
        super(BaseHandler, self).write(data)

    def prepare_arg_dict(self):
        arg_dict = self.request.arguments
        for k, v in arg_dict.items():
            arg_dict[k] = v[0]
        return arg_dict

    # must have
    def data_received(self, chunk):
        super(BaseHandler, self).data_received(chunk)
