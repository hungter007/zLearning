# _*_ coding: utf-8 _*_
from django.conf.urls import url

from .views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView
urlpatterns = [
    url(r'^org_list/$', OrgView.as_view(), name="org_list"),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="home"),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="desc"),
    url(r'^teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="teacher"),

    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),
]