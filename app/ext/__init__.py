#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
from flask_sqlalchemy import SQLAlchemy
from flask_celery import Celery

db              = SQLAlchemy()
celery          = Celery()
