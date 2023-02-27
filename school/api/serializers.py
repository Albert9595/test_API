from .models import Subjects, Groups, Students, Score
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'group_name']


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ['id', 'first_name', 'second_name']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'subject_name']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'score', 'subject_id', 'students_id', 'groups_id']