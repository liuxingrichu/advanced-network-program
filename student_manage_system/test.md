添加讲师
insert into teacher (teacher_name) values ('Jim');


------欢迎进入学员管理系统-------
1 讲师视图
2 学生视图
3 退出系统
--------------end---------------
请输入相关操作：1
请输入讲师名：Jim
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_class
请输入创建班级的名称:S2
请输入创建班级的类型:linux
	班级创建成功!
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_lesson
请输入要添加lesson的班级名:S2
请输入添加的lesson名（类day1）:day1
	课程已存在!
	课程ID：1 课程名：day1
	班级与课程对应关系，添加成功!
	班级ID：2 课程ID：1
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_student
请输入要添加学员的班级名:S1
请输入学员的姓名:Lucy
请输入学员的QQ号:38944343
	学员添加成功!
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_study_record
请输入要添加学习记录的班级名:S1
请输入添加学习记录的课节名（lesson）:day3
	当前上课记录已经创建
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_study_record
请输入要添加学习记录的班级名:S1
请输入添加学习记录的课节名（lesson）:day2
class_obj.students:  [student name: Tom, student name: Oliver, student name: Lucy]
输入学生 Tom 的上课状态（yes/no）：no
	添加学生Tom的上课记录成功！
	班级:S1 课程:python 课节:day2 学生:Tom 上课状态:no
输入学生 Oliver 的上课状态（yes/no）：yes
	添加学生Oliver的上课记录成功！
	班级:S1 课程:python 课节:day2 学生:Oliver 上课状态:yes
输入学生 Lucy 的上课状态（yes/no）：yes
	添加学生Lucy的上课记录成功！
	班级:S1 课程:python 课节:day2 学生:Lucy 上课状态:yes
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：modify_score
请输入学习记录的班级名:S1
请输入学习记录的课节名（lesson）:day1
输入要修改成绩的学生名(q 退出)：Tom
输入修改后的成绩: 92
	修改学生Tom成绩成功，成绩：92
输入要修改成绩的学生名(q 退出)：Oliver
	学生Oliver未考勤记录，请联系讲师！
输入要修改成绩的学生名(q 退出)：Lucy
	学生Lucy未考勤记录，请联系讲师！
输入要修改成绩的学生名(q 退出)：q
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：add_study_record
请输入要添加学习记录的班级名:S1
请输入添加学习记录的课节名（lesson）:day2
	当前上课记录已经创建
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：modify_score
请输入学习记录的班级名:S1
请输入学习记录的课节名（lesson）:day2
输入要修改成绩的学生名(q 退出)：Tom
	学生Tom未上课，无法修改成绩！
输入要修改成绩的学生名(q 退出)：Oliver
输入修改后的成绩: 89
	修改学生Oliver成绩成功，成绩：89
输入要修改成绩的学生名(q 退出)：q
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：show_classes
teacher: Jim
讲师：【Jim】	班级：【S1】	类型：【python】
讲师：【Jim】	班级：【S2】	类型：【linux】
------ 欢迎讲师 Jim 登陆学员管理系统------
add_class            添加班级
add_lesson           添加课节
add_student          添加学员
add_study_record     添加上课记录
modify_score         修改成绩
show_classes         查看所有的班级
exit                 退出
-----------------end------------------
请输入相应操作：exit


------欢迎进入学员管理系统-------
1 讲师视图
2 学生视图
3 退出系统
--------------end---------------
请输入相关操作：2
请输入学员姓名：Tom
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：up_homework
请输入班级名:S1
请输入的课节名（lesson）:day3
	上传成功!
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：show_score
请输入班级名:S1
请输入的课节名（lesson）:day1
班级：【S1】 课节：【day1】 学员：【Tom】 成绩：【92】
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：exit

------欢迎进入学员管理系统-------
1 讲师视图
2 学生视图
3 退出系统
--------------end---------------
请输入相关操作：2
请输入学员姓名：Tom
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：up_homework
请输入班级名:S1
请输入的课节名（lesson）:day2
	未上课，作业无法上传！
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：exit

------欢迎进入学员管理系统-------
1 讲师视图
2 学生视图
3 退出系统
--------------end---------------
请输入相关操作：2
请输入学员姓名：Tom
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：up_homework
请输入班级名:S1
请输入的课节名（lesson）:day1
	作业已上传！
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：show_score
请输入班级名:S1
请输入的课节名（lesson）:day1
班级：【S1】 课节：【day1】 学员：【Tom】 成绩：【92】
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：show_rank
	学员: Tom 排名：1
-----欢迎Tom进入学员管理系统------
up_homework  交作业
show_score   查成绩
show_rank    查排名
exit         退出
--------------end---------------
请输入相应操作：exit
