#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
from sqlalchemy import func
from .models import Student, Lesson, Class_m2m_Lesson, StudyRecord


class StudentCenter(object):
    def __init__(self, session):
        self.session = session
        self.authentication()
        self.handler()
        self.student = None

    def handler(self):
        while True:
            print('\033[36;1m欢迎%s进入学员管理系统'.center(30, '-') %
                  self.student_obj.stu_name)
            print('up_homework  交作业\n'
                  'show_score   查成绩\n'
                  'show_rank    查排名\n'
                  'exit         退出')
            print('end\033[0m'.center(36, '-'))
            func = input('\033[34;1m请输入相应操作：\033[0m').strip()
            if hasattr(self, func):
                getattr(self, func)()

    def authentication(self):
        while True:
            name = input('\033[34;0m请输入学员姓名：\033[0m').strip()
            self.student_obj = self.session.query(Student).filter_by(
                stu_name=name).first()
            if not self.student_obj:
                print('\t\033[31;0m请输入正确的学员姓名！\033[0m')
            else:
                break

    def up_homework(self):
        "上传作业"
        class_name = input("\033[34;0m请输入班级名:\033[0m")

        for class_obj in self.student_obj.classes:
            if class_name == class_obj.class_name:
                lesson_name = input("\033[34;0m请输入的课节名（lesson）:\033[0m")
                lesson_obj = self.session.query(Lesson).filter_by(
                    lesson_name=lesson_name).first()

                if lesson_obj:
                    class_m2m_lesson_obj = self.session.query(
                        Class_m2m_Lesson).filter(
                        Class_m2m_Lesson.class_id == class_obj.class_id). \
                        filter(
                        Class_m2m_Lesson.lesson_id == lesson_obj.lesson_id).first()
                    if class_m2m_lesson_obj:
                        study_record_obj = self.session.query(
                            StudyRecord).filter(
                            StudyRecord.class_m2m_lesson_id == class_m2m_lesson_obj.id).filter(
                            StudyRecord.stu_id == self.student_obj.stu_id).first()

                        if study_record_obj:
                            if study_record_obj.score:
                                print("\t\33[31;1m作业已上传！\33[0m")
                            elif study_record_obj.status == 'yes':
                                score = random.randint(10, 100)
                                study_record_obj.score = score
                                self.session.commit()
                                print("\t\033[32;1m上传成功!\033[0m")
                            else:
                                print("\t\033[31;1m未上课，作业无法上传！\033[0m")
                        else:
                            print("\t\033[31;1m上课记录未创建，请联系讲师！\033[0m")
                    else:
                        print("\t\033[31;1m无相应课时！\33[0m")
                else:
                    print("\t\033[31;1m课节未创建\33[0m")
            else:
                print("\t\033[31;1m班级未创建\33[0m")

    def show_score(self):
        class_name = input("\033[34;0m请输入班级名:\033[0m")

        for class_obj in self.student_obj.classes:
            if class_name == class_obj.class_name:
                lesson_name = input("\033[34;0m请输入的课节名（lesson）:\033[0m")
                lesson_obj = self.session.query(Lesson).filter_by(
                    lesson_name=lesson_name).first()

                if lesson_obj:
                    class_m2m_lesson_obj = self.session.query(
                        Class_m2m_Lesson).filter(
                        Class_m2m_Lesson.class_id == class_obj.class_id). \
                        filter(
                        Class_m2m_Lesson.lesson_id == lesson_obj.lesson_id).first()
                    if class_m2m_lesson_obj:
                        study_record_obj = self.session.query(
                            StudyRecord).filter(
                            StudyRecord.class_m2m_lesson_id == class_m2m_lesson_obj.id).filter(
                            StudyRecord.stu_id == self.student_obj.stu_id).first()
                        if study_record_obj:
                            print('\033[32;1m班级：【%s】 课节：【%s】 学员：【%s】'
                                  ' 成绩：【%s】\033[0m'
                                  % (
                                      class_obj.class_name,
                                      lesson_obj.lesson_name,
                                      self.student_obj.stu_name,
                                      study_record_obj.score
                                  ))
                        else:
                            print("\t\033[31;1m上课记录未创建，请联系讲师！\033[0m")
                    else:
                        print("\t\033[31;1m无相应课时！\33[0m")
                else:
                    print("\t\033[31;1m课节未创建\33[0m")
            else:
                print("\t\033[31;1m班级未创建\33[0m")

    def show_rank(self):
        total_info = self.session.query(func.sum(StudyRecord.score),
                                        StudyRecord.stu_id). \
            group_by(StudyRecord.stu_id).all()
        list_sorted = sorted(total_info, key=lambda x: x[0], reverse=True)
        for element in list_sorted:
            if element[1] == self.student_obj.stu_id:
                print('\t\033[32;1m学员: %s 排名：%s\033[0m' %
                      (self.student_obj.stu_name,
                       list_sorted.index(element) + 1))

    def exit(self):
        exit()
