#!/usr/bin/env python
# -*- coding:utf-8 -*-


from sqlalchemy import create_engine

from models import model_v2
from conf import settings

def syncdb(argvs):
    print("Syncing DB....")
    engine = create_engine(settings.ConnParams, echo=True)
    model_v2.Base.metadata.create_all(engine) #创建所有表结构
