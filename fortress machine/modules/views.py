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


def create_remoteusers(argvs):
    '''
    create remoteusers
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        remoteusers_file = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreate_remoteusers -f <the new remoteusers file>",
            quit=True)
    source = yaml_parser(remoteusers_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = model_v2.RemoteUser(username=val.get('username'),
                                      auth_type=val.get('auth_type'),
                                      password=val.get('password'))
            session.add(obj)
        session.commit()


def create_fortressusers(argvs):
    '''
    create fortress machine access user
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        user_file = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreate_fortressusers -f <the new users file>",
            quit=True)

    source = yaml_parser(user_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = model_v2.FortressUser(username=key,
                                        password=val.get('password'))
            # if val.get('groups'):
            #     groups = session.query(models.Group).filter(
            #         model_v2.Group.name.in_(val.get('groups'))).all()
            #     if not groups:
            #         print_err("none of [%s] exist in group table." % val.get(
            #             'groups'), quit=True)
            #     obj.groups = groups
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            # print(obj)
            session.add(obj)
        session.commit()


def create_groups(argvs):
    '''
    create groups
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        group_file = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreategroups -f <the new groups file>",
            quit=True)
    source = yaml_parser(group_file)
    if source:
        for key, val in source.items():
            print(key, val)
            obj = model_v2.HostGroup(name=key)
            # if val.get('bind_hosts'):
            #     bind_hosts = common_filters.bind_hosts_filter(val)
            #     obj.bind_hosts = bind_hosts
            #
            # if val.get('user_profiles'):
            #     user_profiles = common_filters.user_profiles_filter(val)
            #     obj.user_profiles = user_profiles
            session.add(obj)
        session.commit()


def create_bindhosts(argvs):
    '''
    create bind hosts
    :param argvs:
    :return:
    '''
    if '-f' in argvs:
        bindhosts_file = argvs[argvs.index("-f") + 1]
    else:
        print_err(
            "invalid usage, should be:\ncreate_bindhosts -f <the new bindhosts file>",
            quit=True)
    source = yaml_parser(bindhosts_file)
    if source:
        for key, val in source.items():
            # print(key,val)
            host_obj = session.query(model_v2.Host).filter(
                model_v2.Host.hostname == val.get('hostname')).first()
            assert host_obj
            for item in val['remote_users']:
                print(item)
                assert item.get('auth_type')
                if item.get('auth_type') == 'ssh-password':
                    remoteuser_obj = session.query(model_v2.RemoteUser).filter(
                        model_v2.RemoteUser.username == item.get('username'),
                        model_v2.RemoteUser.password == item.get('password')
                    ).first()
                else:
                    remoteuser_obj = session.query(model_v2.RemoteUser).filter(
                        model_v2.RemoteUser.username == item.get('username'),
                        model_v2.RemoteUser.auth_type == item.get('auth_type'),
                    ).first()
                if not remoteuser_obj:
                    print_err("RemoteUser obj %s does not exist." % item,
                              quit=True)
                bindhost_obj = model_v2.BindHost(host_id=host_obj.id,
                                                 remoteuser_id=remoteuser_obj.id)
                session.add(bindhost_obj)
                # for groups this host binds to
                if source[key].get('groups'):
                    group_objs = session.query(model_v2.HostGroup).filter(
                        model_v2.HostGroup.name.in_(
                            source[key].get('groups'))).all()
                    assert group_objs
                    print('groups:', group_objs)
                    bindhost_obj.hostgroups = group_objs
                # for user_profiles this host binds to
                if source[key].get('fortress_user'):
                    fortressuser_objs = session.query(
                        model_v2.FortressUser).filter(
                        model_v2.FortressUser.username.in_(
                            source[key].get('fortress_user')
                        )).all()
                    assert fortressuser_objs
                    print("fortressuser:", fortressuser_objs)
                    bindhost_obj.fortress_users = fortressuser_objs
                    # print(bindhost_obj)
        session.commit()
