#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by bu on 2017-05-09
"""
from __future__ import unicode_literals
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import Flask
from views import views_configure_blueprint
from app.ext import db
from app.ext import celery

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.settings.production')
    _configure_blueprint(app)
    _configure_extensions(app)
    _configure_logging(app)

    return app

def _configure_blueprint(app):
    views_configure_blueprint(app)

def _configure_extensions(app):
    db.init_app(app)
    celery.init_app(app)
    celery.config_from_object('app.settings.celery_config')

def _configure_logging(app):
    app.logger.setLevel(logging.DEBUG)
    formatter            = logging.Formatter('[%(asctime)s] (%(levelname)s):%(filename)s:%(funcName)s:%(lineno)d: %(message)s')

    debug_log            = os.path.join(app.root_path, app.config['DEBUG_LOG'])
    debug_log_handler    = RotatingFileHandler(debug_log, maxBytes=10000000, backupCount=5)
    debug_log_handler.setLevel(logging.DEBUG)
    debug_log_handler.setFormatter(formatter)
    app.logger.addHandler(debug_log_handler)

    error_log            = os.path.join(app.root_path, app.config['ERROR_LOG'])
    error_log_handler    = RotatingFileHandler(error_log, maxBytes=10000000, backupCount=5)
    error_log_handler.setLevel(logging.ERROR)
    error_log_handler.setFormatter(formatter)
    app.logger.addHandler(error_log_handler)
