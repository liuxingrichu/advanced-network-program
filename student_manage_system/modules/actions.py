#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.orm import sessionmaker

from conf.settings import engine
from .models import Teacher, Class
from .teacher_center import TeacherCenter
from .student_center import StudentCenter


class Action(object):
    def __init__(self):
        session = sessionmaker(bind=engine)
        self.session = session()
        self.init_database()

    def func(self):
        while True:
            print("\033[36;1m欢迎进入学员管理系统\n"
                  "1 讲师视图\n"
                  "2 学生视图\n"
                  "q 退出管理系统\n\033[0m")
            choice = input('请输入相关操作：').strip()
            if choice == '1':
                TeacherCenter(self.session)
            elif choice == '2':
                StudentCenter(self.session)
            elif choice == 'q':
                print('感谢使用学员管理系统，记着下次要来奥!')
                break
            else:
                print('\033[31;1m请输入正常选项\033[0m')

    def init_database(self):
        rest = self.session.query(Teacher).filter(Teacher.teacher_id>0).all
        if not rest:
            class1 = Class(class_name='s12', course='python')
            teacher1 =Teacher(teacher_name='Tom')
            teacher1.classes = [class1]

            self.session.add_all([class1, teacher1])
            self.session.commit()
