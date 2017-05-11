#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
from app.ext import db


class User(db.Model):
    __table_args__ = ({'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8'})

    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False, default='')
