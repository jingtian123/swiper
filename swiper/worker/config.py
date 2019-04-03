#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# @Author :hejing

"""celery配置"""


broker_url = 'redis://127.0.0.1:6379/1'
borker_pool_limit = 100 #  Borker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']

task_serializer = 'pickle'
result_content = 3600  #任务过期时间


result_backend = 'redis://127.0.0.1:6379/1'
result_serializer = 'pickle'
result_cache_max = 1000 # 任务加过最大缓存数量

#日志等级
worker_redirect_stdouts_level = 'INFO'