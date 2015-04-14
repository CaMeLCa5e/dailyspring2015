#! /usr/bin/env python 
import urllib2
import json


locu_api = '#'

url = 'https://api.locu.com/v1_0/venu/search/?locality=Newport'
json_obj = urllib2.urlopen(url)

data = jason.load(json_obj)

print data