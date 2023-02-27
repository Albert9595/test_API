from django.db import models


class Groups(models.Model):
    group_name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self) -> str:
        return self.group_name


class Students(models.Model):
    first_name = models.CharField(max_length=100, blank=True, default='')
    second_name = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self) -> str:
        return self.first_name


class Subjects(models.Model):
    subject_name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self) -> str:
        return self.subject_name


class Score(models.Model):
    score = models.CharField(max_length=100, blank=True, default='')
    groups_id = models.ForeignKey('Groups', related_name='groups', on_delete=models.CASCADE)
    students_id = models.ForeignKey('Students', related_name='students', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subjects', related_name='subjects', on_delete=models.CASCADE)