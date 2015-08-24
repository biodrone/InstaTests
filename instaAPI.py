#!/usr/bin/python

#TODO Restrict search by language (geotag?) or filter out non english ones programmatically
#TODO Put tags and count in 2 different arrays to count how many of each tag there are

from instagram.client import InstagramAPI
from random import randint
import sys
import time
from collections import OrderedDict
from urllib2 import urlopen
import pprint
from sets import Set
from collections import Counter

user_id = "2071972233"
user_token = "2071972233.ab103e5.04668cab8f264287b09e74030d24050c"
client_id = '311da96cc1b7487a83a0fadb2dc6b464'
client_secret = '4394245572c74f11aa0b2046974e9f65'
access_token = '2071972233.311da96.836a5a01111d4c27949e639f30f94673'
client_ip = urlopen('http://ip.42.pl/raw').read()
api = InstagramAPI(client_id=client_id, client_secret=client_secret, client_ips=client_ip, access_token=access_token)

def main():
    #need to try catch for error 200 (not valid response, generally means network issue a.k.a. bt wifi not signed in)
    tagSearch("like4like")
    #tagSearch('animals')
    #tagSearch('fashion')

def tagSearch(sTag):
    tags = []
    tag_search, next_tag = api.tag_search(q=sTag)

    i = 0
    while i < 5:
        tag_recent_media, next = api.tag_recent_media(tag_name=tag_search[0].name)
        for media in tag_recent_media:
            for t in media.tags:
                tags.append(str(t).replace("Tag: ", '', 1))
        i += 1

    tagParse(Counter(tags).most_common(21))

def tagParse(lstTags = []):
    popList = []
    finTags = []
    i = 0
    while i < 20:
        popList.append(lstTags[i])
        i += 1
    for x in popList:
        finTags.append("#" + x[0])
    print(finTags)
def popTest():
    popshits = api.media_popular() #need to search this for tags
    print len(popshits)

    for m in popshits:
        print(m)

    for media in popshits:
        tags = []
        poptags = []
        for tag in media.tags:
            tags.append(tag.name.lower())
            if tag in poptags:
                index = poptags.index(tag)

            print(tag)

    z = [[0 for _ in range(2)] for _ in range(2)]

    pprint.pprint(z)

if __name__ == "__main__":
    main()
