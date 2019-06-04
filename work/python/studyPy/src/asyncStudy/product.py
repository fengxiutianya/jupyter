#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:03
    filename    : product.py
    info        : 用于记录如何部署文件
'''

'''
    导出依赖
    1. 通过pip3导出依赖
        pip3 freeze > requirements.txt
        这个命令会导出当前机器上所有的依赖，也就是输出当前你安装的全部非Python标准库包)
        
    2. 通过pipreqs导出依赖
       pipreqs只导出指定项目下Python文件import的库
       
       安装
       pip3 install pipreqs
       
       切换到指定目录，
       输出到requirements.txt到项目根目录下
       pipreqs --use-local ./
       
    3. 通过pipenv管理依赖
        pip install pipenv安装好库.
        切换到项目根目录
        终端键入Pipenv install
'''