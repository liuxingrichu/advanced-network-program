#!/usr/bin/env python
# -*- coding:utf-8 -*-

from models import model_v2
from modules.utils import print_err
from modules.utils import yaml_parser
from modules.db_conn import session
from modules.db_conn import engine


def syncdb(argvs):
    print("Syncing DB....")
    model_v2.Base.metadata.create_all(engine)  # 创建所有表结构


def create_hosts(argvs):
    '''
    create hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        hosts_file = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreate_hosts -f <the new hosts file>",
            quit=True)
    source = yaml_parser(hosts_file)
    if source:
        print(source)
        for key, val in source.items():
            print(key, val)
            obj = model_v2.Host(hostname=key, ip=val.get('ip'),
                                port=val.get('port') or 22)
            session.add(obj)
        session.commit()
