#!/usr/bin/python

from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict

user_id = "2071972233"
user_token = "2071972233.ab103e5.04668cab8f264287b09e74030d24050c "

def main():
    client_id = '311da96cc1b7487a83a0fadb2dc6b464'
    client_secret = '4394245572c74f11aa0b2046974e9f65'
    access_token = '2071972233.311da96.836a5a01111d4c27949e639f30f94673'
    client_ip = 'YOUR PUBLIC IP'
    api = InstagramAPI(client_id=client_id, client_secret=client_secret,client_ips= client_ip,access_token= access_token)

    all_media_ids = []
    media_ids,next = api.tag_recent_media(tag_name="instagood", count=80)
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

    #remove duplictes if any.
    media_all_ids=list(OrderedDict.fromkeys(media_all_ids))

    print len(media_all_ids)


if __name__ == "__main__":
    main()
