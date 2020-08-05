from django.db import models
from mysite.school.models import Student, Lecturer, Course, Lesson


class LecturerCalendar(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def


class StudentCalendar(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)