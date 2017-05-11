#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
from flask import Blueprint

bp = Blueprint('views.login', __name__)


@bp.route('/')
def hello_world():
    return 'Hello World!'
