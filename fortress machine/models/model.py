#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Column, Integer, String, Enum, ForeignKey, \
    UniqueConstraint, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy_utils import ChoiceType, PasswordType

Base = declarative_base()

# host_m2m_remoteuser = Table('host_m2m_remoteuser', Base.metadata,
#                             Column('host_id', Integer, ForeignKey('host.id')),
#                             Column('remoteuser_id', Integer,
#                                    ForeignKey('romote_user.id'))
#                             )

user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadate,
                          Column('fortress_user_id', Integer,
                                 ForeignKey('fortress_user_id')),
                          Column('bindhost_id', Integer,
                                 ForeignKey('bindhost_id'))
                          )


class BindHost(Base):
    '''
    192.168.1.10 web bj_group
    192.168.1.11 mysql sh_group
    '''
    __tablename__ = 'bind_host'
    # 联合唯一
    __table_args__ = (UniqueConstraint('host_id', 'group_id', 'remoteuser_id',
                                       name='_host_group_remoteuser_uc'),)
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    group_id = Column(Integer, ForeignKey('group.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship('Host', backref='bind_hosts')
    group = relationship('HostGroup', backref='bind_groups')
    remote_user = relationship('RemoteUser', backref='bind_remote_users')

    def __repr__(self):
        return '<%s -- %s -- %s>' % (self.host.id,
                                     self.group.name,
                                     self.remote_user.username)


class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64))
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)
    # remote_users = relationship('RemoteUser', secondary=host_m2m_remoteuser,
    #                             backref='hosts')

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    __tablename__ = 'remote_user'
    # 联合唯一
    __table_args__ = (UniqueConstraint('auth_type', 'username', 'password',
                                       name='_user_passwd_uc'),)

    id = Column(Integer, primary_key=True)
    AuthTypes = [
        ('ssh-password', 'SSH/Password'),
        ('ssh-type', 'SSH/KEY'),
    ]
    auth_type = Column(ChoiceType(AuthTypes))
    # auth_type = Column(Enum(0,1))
    username = Column(String(64))
    password = Column(String(128))

    def __repr__(self):
        return self.username


class FortressUser(Base):
    __tablename__ = 'fortress_user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))
    bind_hosts = relationship('BindHost', secondary='user_m2m_bindhost',
                              backref='fortress_users')

    def __repr__(self):
        return self.username


class AuditLog(Base):
    pass
