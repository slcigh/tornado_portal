import json


def prepare_json(data):
    if isinstance(data, dict):
        items = data.items()
    else:
        items = enumerate(data)
    for k, v in items:
        if isinstance(v, dict) or isinstance(v, list):
            data[k] = prepare_json(v)
        else:
            try:
                json.dumps(v)
            except (TypeError, OverflowError, ValueError):
                data[k] = str(v)
    return data


s1 = {"d": 'i', "ic": "t", "t": 123}
s2 = "str123"
s3 = [1, 2, 3, '14d']

print prepare_json(s1)
print prepare_json(s2)
print prepare_json(s3)
