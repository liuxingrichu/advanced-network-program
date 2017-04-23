#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    orm: 多对多关系
    实现：增删查
"""


from sqlalchemy.orm import sessionmaker
import orm_m2m


# 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
Session_class = sessionmaker(bind=orm_m2m.engine)
session = Session_class()  # 生成session实例

# # 添加
# b1 = orm_m2m.Book(name="learn Python", pub_date='2017-1-1')
# b2 = orm_m2m.Book(name="learn linux", pub_date='2017-1-10')
# b3 = orm_m2m.Book(name="learn network", pub_date='2017-2-1')
# b4 = orm_m2m.Book(name="活法", pub_date='2017-5-1')
#
# a1 = orm_m2m.Author(name="Jim")
# a2 = orm_m2m.Author(name="Jack")
# a3 = orm_m2m.Author(name="Rain")
#
# # 图书与作者的关联关系
# b1.authors = [a1, a2]
# b2.authors = [a1, a2, a3]
# b3.authors = [a2, a3]
#
# session.add_all([b1, b2, b3, b4, a1, a2, a3])


# 通过作者查询书
author_obj = session.query(orm_m2m.Author).filter(
    orm_m2m.Author.name == 'Jim').first()
print(author_obj.books)
print(author_obj.books[0].pub_date)



# 通过书查询作者
print('-' * 60)
book_obj = session.query(orm_m2m.Book).filter(orm_m2m.Book.id == 2).first()
print(book_obj.authors)
book_obj1 = session.query(orm_m2m.Book).filter(
    orm_m2m.Book.name == 'learn Python').first()
print(book_obj1.authors)


# 通过书删除作者
# book_obj.authors.remove(author_obj)

# 通过书删除作者
# author_obj =session.query(orm_m2m.Author).filter_by(name="Jack").first()
# book_obj = session.query(orm_m2m.Book).filter_by(name="learn Python").first()
# book_obj.authors.remove(author_obj) #从一本书里删除一个作者

# 直接删除作者
author_obj = session.query(orm_m2m.Author).filter_by(name="Jack").first()
print(author_obj.name, author_obj.books)
session.delete(author_obj)

session.commit()
