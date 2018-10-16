#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests,time
from store_json import store_json
from ip import blacklist_tools
from global_tools import set_logger

# used to detect sip.
def stopforumspam_toxic_ip_range(mylog):
    requests.adapters.DEFAULT_RETRIES = 5
    try:
        http = requests.get('http://www.stopforumspam.com/downloads/toxic_ip_range.txt', verify=False,timeout=120)
        neir = http.text
        lines = neir.split('\n')
        del lines[-1]
    except Exception, e:
        mylog.warning("download spam timeout!!!")
        lines=[]
    # print lines
    ip_dict = {}
    for line in lines:
        # print line
        ip_dict[line] = {
            'subtype':'spam',
            'desc_subtype':'spam ip;source:http://www.stopforumspam.com/downloads/toxic_ip_range.txt',
            'level':'info',
            'fp':'unknown',
            'status':'unknown',
            'dport': -1,
            'mapping_ip': line,
            'date' : time.strftime('%Y-%m-%d',time.localtime(time.time()))
        }
        # print ip_dict
    return ip_dict

def main():
    mylog=set_logger()
    dict = stopforumspam_toxic_ip_range(mylog)
    #print len(dict)
    store_json(dict, 'stopforumspam_toxic_ip_range')
    #mylog.info("update spam!")

if __name__=="__main__":
    main()