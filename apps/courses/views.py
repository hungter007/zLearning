from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import Course, CourseResource, Video
from operation.models import UserCourse, UserFavorite, CourseComments


class CourseView(View):
    def get(self, request):
        all_courses = Course.objects.all()
        hot_courses = Course.objects.all().order_by("-hot")[:3]
        #热门排序
        sort = request.GET.get('sort', "")
        if sort == "students":
            all_courses = all_courses.order_by("-students")
        elif sort == "hot":
            all_courses = all_courses.order_by("-hot")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 5, request=request)

        courses = p.page(page)
        return render(request, 'course-list.html', {
            "all_courses": courses,
            "sort": sort,
            "hot_courses": hot_courses
        })


class CourseDetialView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        #方法二，直接获取拥有同样课程的用户 --方法一为使用函数返回 见course/models.py
        # all_user_course = UserCourse.objects.all().filter(course_id=int(course_id))
        course.click_nums += 1
        course.save()

        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:2]
        else:
            relate_courses = []

        has_fav_course = False
        has_fav_org = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org.id, fav_type=2):
                has_fav_org = True
        return render(request, 'course-detail.html', {
            "course": course,
            "relate_courses": relate_courses,
            "has_fav_course": has_fav_course,
            "has_fav_org": has_fav_org
        })


class CourseVideoView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        #查询用户是否关联该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        # 拥有该课程的一个UserCourse类实例化对象
        user_courses = UserCourse.objects.filter(course=course)
        # 获取拥有该课程的用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 利用用户id获取所有的id对应学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 根据课程集合，获取所有的课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 根据课程id获取Course这个类对象，用于前端展示
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:2]
        all_resource = CourseResource.objects.filter(id=course.id)
        return render(request, "course-video.html", {
            "course_id": course_id,
            "course": course,
            "all_resource": all_resource,
            "relate_courses": relate_courses
        })


class CommentsView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        all_resource = CourseResource.objects.filter(id=course.id)
        all_comments = CourseComments.objects.filter(course_id=course_id)
        """
        学习该课程的同学还学习
        """
        # 拥有该课程的一个UserCourse类实例化对象
        user_courses = UserCourse.objects.filter(course=course)
        # 获取拥有该课程的用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 利用用户id获取所有的id对应学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 根据课程集合，获取所有的课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 根据课程id获取Course这个类对象，用于前端展示
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:2]
        return render(request, "course-comment.html", {
            "course_id": course_id,
            "course": course,
            "all_resource": all_resource,
            "all_comments": all_comments,
            "relate_courses": relate_courses
        })


class AddCommentsView(View):
    """
    添加用户评论
    """
    def post(self, request):
        if not request.user.is_authenticated():
            return HttpResponse('{"status": "fail", "msg": "用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id", 0)
        comments = request.POST.get("comments", "")
        if int(course_id) > 0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=int(course_id))
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status": "success", "msg": "评论成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail", "msg": "评论出错"}', content_type='application/json')


class VideoPlayView(View):
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        # 查询用户是否关联该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()

        # 拥有该课程的一个UserCourse类实例化对象
        user_courses = UserCourse.objects.filter(course=course)
        # 获取拥有该课程的用户id
        user_ids = [user_course.user.id for user_course in user_courses]
        # 利用用户id获取所有的id对应学过的课程
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 根据课程集合，获取所有的课程id
        course_ids = [user_course.course.id for user_course in all_user_courses]
        # 根据课程id获取Course这个类对象，用于前端展示
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:2]
        all_resource = CourseResource.objects.filter(id=course.id)
        return render(request, "course-play.html", {
            "video_id": video_id,
            "course": course,
            "all_resource": all_resource,
            "relate_courses": relate_courses,
            "video": video
        })