# _*_ coding:utf-8 _*_
__author__ = 'Vevid'
__date__ = '2017/10/19 9:55'
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['city', 'name', 'desc', 'add_time']
    search_fields = ['city', 'name', 'desc', 'add_time']
    list_filter = ['city', 'name', 'desc', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position',  'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position',  'add_time']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position',  'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)

