#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .models import Teacher, Class, Student, Class_m2m_Lesson, Lesson, \
    StudyRecord


class TeacherCenter(object):
    def __init__(self, session):
        self.session = session
        self.authentication()
        self.handler()

    def handler(self):
        while True:
            print('\033[36;0m 欢迎讲师 %s 登陆学员管理系统'.center(36, '-')
                  % self.teacher_obj.teacher_name)
            print('add_class            添加班级\n'
                  'add_lesson           添加课节\n'
                  'add_student          添加学员\n'
                  'add_study_record     添加上课记录\n'
                  'modify_score         修改成绩\n'
                  'show_classes         查看所有的班级\n'
                  'exit                 退出')
            print('end\033[0m'.center(42, '-'))
            func = input('请输入相应操作：').strip()
            if hasattr(self, func):
                getattr(self, func)()

    def authentication(self):
        '''认证'''
        while True:
            teacher_name = input('请输入讲师名：').strip()
            self.teacher_obj = self.session.query(Teacher).filter_by(
                teacher_name=teacher_name).first()
            if not self.teacher_obj:
                print("\t\33[31;1m输入错误：请输入有效的讲师名!\033[0m")
            else:
                break

    def add_class(self):
        '''添加班级'''
        class_name = input("\033[34;0m请输入创建班级的名称:\033[0m").strip()
        course = input("\033[34;0m请输入创建班级的类型:\033[0m").strip()
        class_obj = self.session.query(Class).filter_by(
            class_name=class_name).first()
        if not class_obj:
            class_new = Class(class_name=class_name, course=course)
            self.teacher_obj.classes.append(class_new)

            self.session.add(class_new)
            self.session.commit()
            print("\t\033[32;1m班级创建成功!\033[0m")
        else:
            print("\t\033[31;1m班级已经存在!\033[0m")

    def add_student(self):
        '''添加学员'''
        class_name = input("\033[34;0m请输入要添加学员的班级名:\033[0m").strip()
        class_obj = self.session.query(Class).filter_by(
            class_name=class_name).first()
        if class_obj and class_obj.teachers[0] == self.teacher_obj:
            stu_name = input("\033[34;0m请输入学员的姓名:\033[0m")
            QQ = input("\033[34;0m请输入学员的QQ号:\033[0m")
            student_obj = self.session.query(Student).filter_by(
                stu_name=stu_name).first()

            if not student_obj:
                student_new = Student(stu_name=stu_name, QQ=QQ)
                class_obj.students.append(student_new)
                self.session.add(student_new)
                self.session.commit()
                print("\t\033[32;1m学员添加成功!\033[0m")

            else:
                print("\t\033[31;1m学员已经存在!\033[0m")
        else:
            print("\t\033[31;1m班级不存在或没有权限管理此班级\033[0m")

    def add_lesson(self):
        '''添加课程节次'''
        class_name = input("\033[34;0m请输入要添加lesson的班级名:\033[0m").strip()
        class_obj = self.session.query(Class).filter_by(
            class_name=class_name).first()

        # 输入的班级名存在且在属于当前老师管理
        if class_obj and class_obj.teachers[0] == self.teacher_obj:
            lesson_name = input("\033[34;0m请输入添加的lesson名（类day1）:\033[0m")
            lesson_obj = self.session.query(Lesson).filter_by(
                lesson_name=lesson_name).first()
            if not lesson_obj:
                lesson_obj = Lesson(lesson_name=lesson_name)
                self.session.add(lesson_obj)
                self.session.commit()
                print('\t\033[32;1m课程添加成功!\033[0m')
                print('\t\033[32;1m课程ID：%s 课程名：%s\033[0m' %
                      (lesson_obj.lesson_id, lesson_obj.lesson_name))
            else:
                print('\t\033[36;1m课程已存在!\033[0m')
                print('\t\033[36;1m课程ID：%s 课程名：%s\033[0m' %
                      (lesson_obj.lesson_id, lesson_obj.lesson_name))

            rest = self.session.query(Class_m2m_Lesson).filter(
                Class_m2m_Lesson.class_id == class_obj.class_id). \
                filter(
                Class_m2m_Lesson.lesson_id == lesson_obj.lesson_id).first()
            if not rest:
                class_m2m_lesson_new = Class_m2m_Lesson(
                    class_id=class_obj.class_id, lesson_id=lesson_obj.lesson_id)
                self.session.add(class_m2m_lesson_new)  # 创建class_m2m_lesson对应关系
                self.session.commit()
                print('\t\033[32;1m班级与课程对应关系，添加成功!\033[0m')
                print('\t\033[32;1m班级ID：%s 课程ID：%s\033[0m' %
                      (class_obj.class_id, lesson_obj.lesson_id))

            else:
                print('\t\033[36;1m班级与课程对应关系，已存在!\033[0m')
                print('\t\033[36;1m班级ID：%s 课程ID：%s\033[0m' %
                      (class_obj.class_id, lesson_obj.lesson_id))
        else:
            print("\t\033[31;1m输入错误：班级不存在或没有权限管理此班级\033[0m")

    def add_study_record(self):
        '''添加学习记录'''
        class_name = input("\033[34;0m请输入要添加学习记录的班级名:\033[0m")
        class_obj = self.session.query(Class).filter_by(
            class_name=class_name).first()
        # 输入的班级名存在且在属于当前老师管理
        if class_obj and class_obj.teachers[0] == self.teacher_obj:
            lesson_name = input("\033[34;0m请输入添加学习记录的课节名（lesson）:\033[0m")
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
                        StudyRecord).filter_by(
                        class_m2m_lesson_id=class_m2m_lesson_obj.id).first()
                    if not study_record_obj:
                        print("class_obj.students: ", class_obj.students)
                        # class_students = self.session.query(
                        #     class_m2m_student).filter_by(
                        #     class_name=class_name).all()
                        # print("class_students: ", class_students)
                        for student_obj in class_obj.students:
                            status = input("输入学生 %s 的上课状态（yes/no）："
                                           % student_obj.stu_name)
                            study_record_new = StudyRecord(
                                class_m2m_lesson_id=class_m2m_lesson_obj.id,
                                stu_id=student_obj.stu_id,
                                status=status)
                            self.session.add(study_record_new)
                            self.session.commit()
                            print('\t\033[32;1m添加学生%s的上课记录成功！\033[0m'
                                  % student_obj.stu_name)
                            print('\t\033[32;1m班级:%s 课程:%s 课节:%s 学生:%s '
                                  '上课状态:%s \033[0m'
                                  % (class_obj.class_name, class_obj.course,
                                     lesson_obj.lesson_name,
                                     student_obj.stu_name,
                                     status))
                    else:
                        print("\t\033[36;1m当前上课记录已经创建\033[0m")
                else:
                    print("\t\033[31;1m系统错误：当前班级的lesson课节未创建\033[0m")
            else:
                print("\t\033[31;1m系统错误：lesson未创建\033[0m")
        else:
            print("\t\033[31;1m输入错误：班级不存在或没有权限管理此班级\033[0m")

    def modify_score(self):
        '''修改成绩'''
        class_name = input("\033[34;0m请输入学习记录的班级名:\033[0m")
        class_obj = self.session.query(Class).filter_by(
            class_name=class_name).first()

        # 输入的班级名存在且在属于当前老师管理
        if class_obj and class_obj.teachers[0] == self.teacher_obj:
            lesson_name = input("\033[34;0m请输入学习记录的课节名（lesson）:\033[0m")
            lesson_obj = self.session.query(Lesson).filter_by(
                lesson_name=lesson_name).first()

            if lesson_obj:
                class_m2m_lesson_obj = self.session.query(
                    Class_m2m_Lesson).filter(
                    Class_m2m_Lesson.class_id == class_obj.class_id). \
                    filter(
                    Class_m2m_Lesson.lesson_id == lesson_obj.lesson_id).first()

                if class_m2m_lesson_obj:
                    while True:
                        # study_record_objs = self.session.query(StudyRecord). \
                        #     filter(StudyRecord.class_m2m_lesson_id ==
                        #            class_m2m_lesson_obj.id).all()
                        # for obj in study_record_objs:
                        #     print(obj)

                        student_name = input(
                            "\033[34;0m输入要修改成绩的学生名(q 退出)：\033[0m")
                        if student_name == "q" or student_name == "Q":
                            break
                        student_obj = self.session.query(Student).filter_by(
                            stu_name=student_name).first()
                        if student_obj:
                            study_record_obj = self.session.query(
                                StudyRecord).filter(
                                StudyRecord.class_m2m_lesson_id == class_m2m_lesson_obj.id).filter(
                                StudyRecord.stu_id == student_obj.stu_id).first()

                            if study_record_obj:
                                if study_record_obj.status == 'yes':
                                    score = input("\033[34;0m输入修改后的成绩: \033[0m")
                                    study_record_obj.score = score
                                    self.session.commit()
                                    print('\t\033[32;1m修改学生%s成绩成功，成绩：%s'
                                          % (student_obj.stu_name, score))
                                else:
                                    print('\t\033[31;0m学生%s未上课，无法修改成绩！'
                                          '\033[0m' % student_name)
                            else:
                                print('\t\033[31;0m学生%s未考勤记录，请联系讲师！'
                                      '\033[0m' % student_name)

                    else:
                        print("\33[31;1m当前上课记录已经创建\33[0m")
                else:
                    print("\33[31;1m系统错误：当前班级的lesson课节未创建\33[0m")
            else:
                print("\33[31;1m系统错误：lesson未创建\33[0m")
        else:
            print("\33[31;1m输入错误：班级不存在或没有权限管理此班级\33[0m")

    def show_classes(self):
        '''查看所有的班级'''
        print(self.teacher_obj)
        for class_obj in self.teacher_obj.classes:
            print("讲师：【%s】\t班级：【%s】\t类型：【%s】" % (
                class_obj.teachers[0].teacher_name,
                class_obj.class_name, class_obj.course))

    def show_students(self):
        pass

    def exit(self):
        exit()
