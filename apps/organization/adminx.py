# _*_ coding: utf-8 _*_
import xadmin

from .models import CityDict, Teacher, CourseOrg


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'des', 'click_nums', 'fav_nums', 'address', 'image', 'city', 'add_time']
    search_fields = ['name', 'des', 'click_nums', 'fav_nums', 'address', 'image', 'city']
    list_filter = ['name', 'des', 'click_nums', 'fav_nums', 'address', 'image', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_yaers', 'work_company', 'work_position', 'points', 'age', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_yaers', 'work_company', 'work_position', 'points', 'age', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_yaers', 'work_company', 'work_position', 'points', 'age', 'click_nums', 'fav_nums', 'add_time']

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
