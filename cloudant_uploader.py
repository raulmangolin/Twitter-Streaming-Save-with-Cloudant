#!/usr/bin/python
# -*- coding: utf-8 -*-

import cloudant
import json

# Cloudant Keys
USERNAME = ''
PASSWORD = ''
account = cloudant.Account(USERNAME)

login = account.login(USERNAME, PASSWORD)
assert login.status_code == 200

db = account.database('tweets')
same_db = account['tweets']
assert db.uri == same_db.uri

def insertTweet(tweet):
    parsed_json = json.loads(tweet)
    parsed_json['_id'] = parsed_json['id_str']

    doc = db.document(parsed_json['id_str'])
    doc.put(params=parsed_json)

    return True

