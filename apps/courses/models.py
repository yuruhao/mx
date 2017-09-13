# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'机构', null=True, blank=True)
    course_teacher = models.ForeignKey(Teacher, verbose_name=u'课程教师', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u'课程名')
    dsc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    course_notice = models.CharField(max_length=50, verbose_name=u'课程公告', null=True, blank=True)
    degree = models.CharField(choices=(('cj',u'初级'),('zj',u'中级'),('gj',u'高级')), max_length=5, verbose_name=u'难度等级')
    learn_times = models.IntegerField(default=0, verbose_name=u'学习时长（分钟数）')
    students = models.IntegerField(default=0, verbose_name=u'学习人数')
    fav_nums = models.IntegerField(default=0, verbose_name=u'收藏人数')
    category = models.CharField(default=u'后端开发', max_length=20, verbose_name=u'课程类别')
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name=u'封面', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    tag = models.CharField(default="", verbose_name=u'课程标签', max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程'
        verbose_name_plural = verbose_name

    def get_zj_nums(self):
        # 获取课程章节数
        return self.lesson_set.all().count()
    def get_learn_students(self):
        # 获取学习用户数量
        return self.usercourse_set.all()[:5]

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节'
        verbose_name_plural = verbose_name

    def get_video_name(self):
        '''获取课程信息名称'''
        return self.video_set.all()

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频'
        verbose_name_plural = verbose_name

        def __unicode__(self):
            return self.name


class CourseRecourse(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'课程')
    name = models.CharField(max_length=100, verbose_name=u'名称')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name=u'资源文件', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

        def __unicode__(self):
            return self.name