#!/usr/bin/env python
# coding=UTF-8

import urllib
import urllib2
import json
import sys

#目录
path = sys.path[0]
print path

#加载配置文件
with open("%s/config.json" % path) as file:
    config = file.read()
    config = json.loads(config)


def saveFile(data):
    try:
        with open("%s/version" % path, "w") as file:
            file.write(data)
    except Exception, e:
        print Exception,":",e

def readFile():
    try:
        with open("%s/version" % path) as file:
            return file.read()
    except Exception, e:
        print Exception,":",e
        
def get():
    url = config["ipipUrl"] + config['token']
    url2 = url + "&a=version"
    req = urllib2.Request(url2)
    res = urllib2.urlopen(req)
    res = res.read()
    if res != readFile():
        saveFile(res)
        download(url)
        print "update"
    else:
        print "noup"

def download(url):
    f = urllib2.urlopen(url) 
    with open("%s/17monipdb.dat" % path, "wb") as code:
	code.write(f.read())

if __name__ == "__main__":
    res = get()
