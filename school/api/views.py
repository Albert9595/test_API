import requests
from collections import defaultdict
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
    data = {}
    number_dict = defaultdict(lambda:{'count': 0, 'avg': 0})
    
    score = Score.objects.filter(students_id=students_id)
    student= Students.objects.filter(id=students_id)
    student_name = [name.first_name for name in student]

    for score_info in score:
        if str(score_info.students_id) == str(student_name[0]):
            number_dict[str(score_info.subject_id)]['avg'] += int(score_info.score)
            number_dict[str(score_info.subject_id)]['count'] += 1
            data[str(score_info.subject_id)] = {
                'studen_name': student_name[0] if student_name else None,
                'avg_score': None,
                'group': str(score_info.groups_id),   
            }

    for subject_name, avg_ifo in number_dict.items():
        avg = avg_ifo['avg'] / avg_ifo['count']
        data[subject_name]['avg_score'] = avg

    return Response(data)


@api_view(('GET',))
def group_sort(requests, groups_id: int) -> dict:
    data = {}
    number_dict = defaultdict(lambda:{'count': 0, 'avg': 0})
    
    score = Score.objects.filter(groups_id=groups_id)

    for score_info in score:
        number_dict[str(score_info.subject_id)]['avg'] += int(score_info.score)
        number_dict[str(score_info.subject_id)]['count'] += 1
        data[str(score_info.subject_id)] = {
            'avg_score': None,
            'group': str(score_info.groups_id)
        }

    for avg_score, avg_ifo in number_dict.items():
        avg = avg_ifo['avg'] / avg_ifo['count']
        data[avg_score]['avg_score'] = avg
    
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
                    return redirect(reverse("landing"))
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def landing(request):
    students = Students.objects.all()
    student_id = {student_id.id: student_id for student_id in students}

    groups = Groups.objects.all()
    groups_id = {groups_id.id: groups_id for groups_id in groups}

    data = {
        'students': student_id,
        'groups': groups_id
    }

    return render(request, 'landing/landing.html', {'data': data})