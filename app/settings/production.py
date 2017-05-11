#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
from default import *


SQLALCHEMY_DATABASE_URI = 'mysql://root:root@flask_demo_db/flask_demo'
SQLALCHEMY_ECHO = True

CELERY_BROKER_URL = 'amqp://flask_demo:72R6M86gnRaLfrq@flask_demo_mq:5672/flask_demo_host'

#CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

REDIS = {
    'host': 'localhost',
    'port': 6379,
    'db': 0,
    'password': ''
}