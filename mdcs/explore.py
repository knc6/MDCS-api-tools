#! /usr/bin/env python
import requests
from collections import OrderedDict

def select_all(host,user,pswd,cert=None,format=None):
    url = host.strip("/") + "/rest/explore/select/all"
    params = dict()
    if format: params['dataformat'] = format
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json(object_pairs_hook=OrderedDict)

def select(host,user,pswd,cert=None,format=None,ID=None,template=None,title=None):
    url = host.strip("/") + "/rest/explore/select"
    params = dict()
    if format:   params['dataformat'] = format
    if ID:       params['id']         = ID
    if template: params['schema']     = template
    if title:    params['title']      = title
    r = requests.get(url, params=params, auth=(user, pswd), verify=cert)
    return r.json(object_pairs_hook=OrderedDict)
    
def delete(ID,host,user,pswd,cert=None):
    """Delete an entry
    
    Input:
        ID - string, ID of object to be deleted
        host - string, URL of MDCS instance
        user - string, username of desired account on MDCS server
        pswd - string, password of desired account on MDCS server
        cert - string, path to authentication certificate
    Output:
        response from MDCS
    """
    
    url = host.strip("/") + "/rest/explore/delete"
    params = dict()
    params['id']=ID
    r = requests.delete(url, params=params, auth=(user, pswd), verify=cert)
    if int(r.status_code)==204:
        return "Successful deletion of: "+ID
    else:
        return r.json()
    
def query(host,user,pswd,cert=None,format=None,query=None,repositories=None):
    url = host.strip("/") + "/rest/explore/query-by-example"
    data = dict()
    if format: data['dataformat'] = format
    if query: data['query'] = query
    if repositories: data['repositories'] = repositories
    r = requests.post(url, data=data, auth=(user, pswd), verify=cert)
    return r.json(object_pairs_hook=OrderedDict)