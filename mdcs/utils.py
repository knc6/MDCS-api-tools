#! /usr/bin/env python
from collections import OrderedDict

def check_response(response):
    try:
        response_json = response.json(object_pairs_hook=OrderedDict)
    except:
        response_json = None
    return response.status_code,r.text,response_json