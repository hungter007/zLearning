# _*_ coding: utf-8 _*_
from django.conf.urls import url

from .views import CourseView, CourseDetialView, CourseVideoView, CommentsView, AddCommentsView, VideoPlayView

urlpatterns = [
    url(r'^list/$', CourseView.as_view(), name="course_list"),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetialView.as_view(), name="course_detail"),
    url(r'^video_list/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name="course_video"),
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comment"),
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
    url(r'^video/(?P<video_id>\d+)/$', VideoPlayView.as_view(), name="video_play"),
]
