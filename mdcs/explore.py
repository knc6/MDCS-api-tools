#! /usr/bin/env python
import requests
import json

def select_all(host,user,pswd,cert=None,format=None):
    url = host + "/rest/explore/select/all"
    params = dict()
    if format: params['dataformat'] = format
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json()

def select(host,user,pswd,cert=None,format=None,ID=None,template=None,title=None):
    url = host + "/rest/explore/select"
    params = dict()
    if format:   params['dataformat'] = format
    if ID:       params['id']         = ID
    if template: params['schema']     = template
    if title:    params['title']      = title
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json()
    
def delete():
    print "This feature has not been added"
    return None
    
def query():
    return None
    print "This feature has not been added"