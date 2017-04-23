#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一本书可以有多个作者，一个作者又可以出版多本书


from sqlalchemy import Table, Column, Integer, String, DATE, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

# 创建books表和authors表之间的关联
# 因该管理不用人工进行操作，故选择使用Table方式创建表
book_m2m_author = Table('book_m2m_author', Base.metadata,
                        Column('book_id', Integer, ForeignKey('books.id')),
                        Column('author_id', Integer, ForeignKey('authors.id')),
                        )


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))
    pub_date = Column(DATE)
    # 关联关系
    authors = relationship('Author', secondary=book_m2m_author, backref='books')

    def __repr__(self):
        return self.name


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))

    def __repr__(self):
        return self.name


# UTF8方式连接mysql数据库
engine = create_engine(
    "mysql+pymysql://admin:*@192.168.*.*/testdb?charset=utf8",
    # echo=True
)
Base.metadata.create_all(engine)
