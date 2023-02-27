import requests
from . import serializers
from .models import Subjects, Groups, Students, Score
from .forms import LoginForm
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse



# User
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


# Subjects
class SubjectsList(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = serializers.SubjectSerializer


# Groups
class GroupsList(generics.ListCreateAPIView):
    queryset = Groups.objects.all()
    serializer_class = serializers.GroupSerializer


# Students
class StudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = serializers.StudentsSerializer


# Score
class ScoreList(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = serializers.ScoreSerializer


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Score.objects.all()
    serializer_class = serializers.ScoreSerializer


@api_view(('GET',))
def student_sort(requests, students_id: int) -> dict:
    group_name = None
    subjects_name = None

    score = Score.objects.filter(students_id=students_id)

    student= Students.objects.filter(id=students_id)
    student_name = [name.first_name for name in student]

    group_id = [group.groups_id for group in score]
    if group_id:
        group = Groups.objects.filter(id=group_id[0].id)
        group_name = [group_name.group_name for group_name in group]

    subject_id = [subjects.subject_id for subjects in score]
    if subject_id:
        subjects = Subjects.objects.filter(id=subject_id[0].id)
        subjects_name = [subjects_name.subject_name for subjects_name in subjects]
   
    number_list = [int(avg_student.score) for avg_student in score]
    avg = sum(number_list)/len(number_list) if number_list else None
    
    data = {
        'studen_name': student_name[0] if student_name else None,
        'avg_score': avg,
        'group': group_name[0] if group_name else None,
        'subjects': subjects_name[0] if subjects_name else None,
    }
    
    return Response(data)


@api_view(('GET',))
def group_sort(requests, groups_id: int) -> dict:
    group_name = None
    subjects_name = None
    
    score = Score.objects.filter(groups_id=groups_id)
    number_list = [int(avg_student.score) for avg_student in score]
    avg = sum(number_list)/len(number_list) if number_list else None

    group_id = [group.groups_id for group in score]
    if group_id:
        group = Groups.objects.filter(id=group_id[0].id)
        group_name = [group_name.group_name for group_name in group]

    subject_id = [subjects.subject_id for subjects in score]
    if subject_id:
        subjects = Subjects.objects.filter(id=subject_id[0].id)
        subjects_name = [subjects_name.subject_name for subjects_name in subjects]
   
    data = {
        'avg_score': avg,
        'group': group_name[0] if group_name else None,
        'subjects': subjects_name[0] if subjects_name else None,
    }
    
    return Response(data)


def user_login(request) -> dict:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse("swagger-ui"))
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

