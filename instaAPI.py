#!/usr/bin/python

from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict

user_id = ""
user_token = ""

#signed header stuff
def main():
    client_id = 'XXXXX'
    client_secret = 'XXXXX'
    access_token = 'XXXXXXX'
    client_ip = 'YOUR PUBLIC IP'
    api = InstagramAPI(client_id=client_id, client_secret=client_secret,client_ips= client_ip,access_token= access_token)
    return

def tag_search(sTag):
    all_media_ids = []
    media_ids,next = api.tag_recent_media(tag_name=sTag, count=80)
    temp,max_tag=next.split('max_tag_id=')
    max_tag=str(max_tag)
    return


for media_id in media_ids:
		all_media_ids.append(media_id.id)
print all_media_ids
print len(all_media_ids)
counter = 1

while next and counter < 3:
	more_media, next =api.tag_recent_media(tag_name='instadogs', max_tag_id=max_tag)
	temp,max_tag=next.split('max_tag_id=')
	max_tag=str(max_tag)
	for media_id2 in more_media:
		all_media_ids.append(media_id2.id)
	counter+=1