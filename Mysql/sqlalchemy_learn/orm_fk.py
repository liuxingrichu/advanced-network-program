#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DATE, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("mysql+pymysql://admin:*@192.168.*.*/testdb",
                       encoding='utf-8',
                       # echo=True
                       )

Base = declarative_base()  # 生成orm基类


class Student(Base):
    '''
    student表
    '''
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    register_date = Column(DATE, nullable=False)

    def __repr__(self):
        return "<%s name: %s>" % (self.id, self.name)


class StudentRecord(Base):
    '''
    student_record表
    '''
    __tablename__ = 'student_record'
    id = Column(Integer, primary_key=True)
    day = Column(Integer, nullable=False)
    status = Column(String(32), nullable=False)
    # 外键关联：表名.列名
    stu_id = Column(Integer, ForeignKey('student.id'))

    # 内存中的关联关系，相当于
    # student = query(Student).filter(Student.id == stu_obj.stu_id).first()
    student = relationship('Student', backref='my_study_record')

    def __repr__(self):
        return '<%s day: %s status: %s>' % (
            self.student.name, self.day, self.status)


# 创建表结构
Base.metadata.create_all(engine)

# 生成实例
Session_class = sessionmaker(bind=engine)
Session = Session_class()

# # 添加表内容
# s1 = Student(name='Tom', register_date='2016-06-06')
# s2 = Student(name='Lucy', register_date='2015-06-05')
# s3 = Student(name='Oliver', register_date='2016-06-07')
# s4 = Student(name='Jack', register_date='2016-06-08')
#
# student_obj1 = StudentRecord(day=1, status='YES', stu_id=1)
# student_obj2 = StudentRecord(day=2, status='NO', stu_id=1)
# student_obj3 = StudentRecord(day=3, status='YES', stu_id=1)
# student_obj4 = StudentRecord(day=1, status='YES', stu_id=2)
#
# Session.add_all(
#     [s1, s2, s3, s4, student_obj1, student_obj2, student_obj3, student_obj4])

# 查询
student_obj = Session.query(Student).filter(Student.name == 'Tom').first()
print(student_obj.my_study_record)

Session.commit()
