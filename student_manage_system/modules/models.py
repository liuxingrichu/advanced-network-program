#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import Integer, String, Column, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from conf.settings import engine

Base = declarative_base()

teacher_m2m_class = Table('teacher_m2m_class', Base.metadata,
                          Column('teacher_id', Integer,
                                 ForeignKey('teacher.teacher_id')),
                          Column('class_id', Integer,
                                 ForeignKey('class.class_id'))
                          )

class_m2m_student = Table('class_m2m_student', Base.metadata,
                          Column('class_id', Integer,
                                 ForeignKey('class.class_id')),
                          Column('stu_id', Integer,
                                 ForeignKey('student.stu_id'))
                          )


class Class_m2m_Lesson(Base):
    __tablename__ = 'class_m2m_lesson'
    id = Column(Integer, primary_key=True)
    class_id = Column(Integer, ForeignKey('class.class_id'))
    lesson_id = Column(Integer, ForeignKey('lesson.lesson_id'))

    classes = relationship('Class', backref='class_m2m_lesson')
    lessons = relationship('Lesson', backref='class_m2m_lesson')

    def __repr__(self):
        return '%s %s' % (self.classes, self.lessons)


class StudyRecord(Base):
    __tablename__ = 'study_record'
    id = Column(Integer, primary_key=True)
    class_m2m_lesson_id = Column(Integer, ForeignKey('class_m2m_lesson.id'))
    stu_id = Column(Integer, ForeignKey('student.stu_id'))
    status = Column(String(32), nullable=False)
    score = Column(Integer, nullable=True)

    class_m2m_lessons = relationship('Class_m2m_Lesson',
                                     backref='my_study_record')
    students = relationship('Student', backref='my_study_record')

    def __repr__(self):
        return '%s status: %s score: %s' % (
            self.stu_id, self.status, self.score)


class Teacher(Base):
    __tablename__ = 'teacher'
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(32), nullable=False, unique=True)

    classes = relationship('Class', secondary=teacher_m2m_class,
                           backref='teachers')

    def __repr__(self):
        return 'teacher: %s' % self.teacher_name


class Student(Base):
    __tablename__ = 'student'
    stu_id = Column(Integer, primary_key=True)
    stu_name = Column(String(32), nullable=False, unique=True)
    QQ = Column(Integer, nullable=False)

    def __repr__(self):
        return 'student name: %s' % self.stu_name


class Class(Base):
    __tablename__ = 'class'
    class_id = Column(Integer, primary_key=True)
    class_name = Column(String(32), nullable=False, unique=True)
    course = Column(String(32), nullable=False)

    students = relationship('Student', secondary=class_m2m_student,
                            backref='classes')

    def __repr__(self):
        return 'class name: %s' % self.class_name


class Lesson(Base):
    __tablename__ = 'lesson'
    lesson_id = Column(Integer, primary_key=True)
    lesson_name = Column(String(32), nullable=False, unique=True)

    def __repr__(self):
        return 'lesson name: %s' % self.lesson_name


Base.metadata.create_all(engine)
