#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author :hejing

import os

from celery import Celery
from worker import config


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

# 创建celery
celery_app = Celery('swiper')

celery_app.config_from_object(config)

celery_app.autodiscover_tasks()