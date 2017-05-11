#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-04-26
"""
from __future__ import unicode_literals
from celery.schedules import crontab

# celery config
CELERY_IMPORTS = (
    'app.tasks',
    'app.schedules'
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_QUEUES = {
    'schedules_queue': {
        'exchange': 'schedules_exchange',
        'exchange_type': 'direct',
        'binding_key': 'schedules_route_key',
    },
    'default': {
        'exchange': 'default',
        'exchange_type': 'direct',
        'binding_key': 'default',
    }

}

CELERY_ROUTES = {
    'app.schedules.*': {
        'queue': 'schedules_queue',
        'binding_key': 'schedules_route_key'
    },
    'default': {
        'queue': 'default',
        'binding_key': 'default'
    }
}

CELERYBEAT_SCHEDULE = {
    'update_sign_in_log_schedule': {
        'task': 'app.schedules.user.update_sign_in_log_schedule',
        'schedule': crontab(minute=0, hour=3),
    },
    'init_btc_hot_wallet_address_schedule': {
        'task': 'app.schedules.bank.init_btc_hot_wallet_address_schedule',
        'schedule': crontab(minute=1, hour=3),
    },

}

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24 * 7
CELERY_IGNORE_RESULT = True
