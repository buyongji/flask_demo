#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
from test import bp as test_bp

def views_configure_blueprint(app):
    app.register_blueprint(test_bp, url_prefix='/test')
