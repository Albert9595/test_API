# Generated by Django 4.1.7 on 2023-02-27 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_students_student_students_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, default='', max_length=100)),
                ('groups_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.groups')),
                ('students_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.subjects')),
            ],
        ),
    ]
