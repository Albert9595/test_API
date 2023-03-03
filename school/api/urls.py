from . import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.user_login,),
    path('users/', views.UserList.as_view()),
    path('landing', views.landing, name='landing'),
    path('subjects/', views.SubjectsList.as_view()),
    path('groups/', views.GroupsList.as_view()),
    path('students/', views.StudentsList.as_view()),
    path('students_sort/<int:students_id>/', views.student_sort),
    path('group_sort/<int:groups_id>/', views.group_sort),
    path('score/', views.ScoreList.as_view(), name='score'),
    path('score/<int:pk>/', views.ScoreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)