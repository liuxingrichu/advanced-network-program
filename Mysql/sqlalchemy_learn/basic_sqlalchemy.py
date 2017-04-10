#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin:*@192.168.*.*/testdb",
                       encoding='utf-8',
                       # echo=True
                       )

Base = declarative_base()  # 生成orm基类


class User(Base):
    __tablename__ = 'user'  # 表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):
        return "<User(name='%s',  password='%s')>" % (
            self.name, self.password)


# Base.metadata.create_all(engine)  # 创建表结构

# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=engine)
Session = Session_class()  # 生成session实例

# # 添加
# user_obj = User(name="Oliver", password="1000110011")  # 生成你要创建的数据对象
# print(user_obj.name, user_obj.id)  # 此时还没创建对象呢，不信你打印一下id发现还是None
#
# Session.add(user_obj)  # 把要创建的数据对象添加到这个session里， 一会统一创建
# print(user_obj.name, user_obj.id)  # 此时也依然还没创建
#
# # 确认提交，后面有相应语句也会做提交
# Session.commit()  # 现此才统一提交，创建数据

# # 查询
# my_user = Session.query(User).filter_by(name="Oliver").first()
# print(my_user)
# print(my_user.id, my_user.name, my_user.password)


# 修改
# my_user = Session.query(User).filter_by(name="Oliver").first()
# my_user.name = "Oliver Li"
# Session.commit()

# 获取全部数据
# print(Session.query(User.name,User.id).all() )

# 多条件查询
objs = Session.query(User).filter(User.id > 1).filter(User.id < 4).all()
for obj in objs:
    print(obj)

# 统计
num = Session.query(User).filter(User.name.like("Ol%")).count()
print('total:', num)

# 分组
from sqlalchemy import func

print(Session.query(func.count(User.name), User.name).group_by(User.name).all())
