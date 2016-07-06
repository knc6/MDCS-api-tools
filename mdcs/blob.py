#! /usr/bin/env python
import requests

def upload(name,host,user,pswd,cert=None):
    url = host.strip("/") + "/rest/blob"
    files = {'blob':open(name, 'rb')}
    r = requests.post(url, files=files, auth=(user, pswd), verify=cert)
    return check_response(r)