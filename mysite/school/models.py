from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Lecturer(CustomUser):
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Lecturers'


class Student(CustomUser):
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = 'Students'


class Course(models.Model):
    students = models.ManyToManyField(Student)
    name = models.CharField(max_length=60)
    tittle = models.CharField(max_length=150)
    # timetable = models.ForeignKey('TimeTable', on_delete=models.CASCADE)
    lecturers = models.ManyToManyField(Lecturer, through='Lesson')


class Lesson(models.Model):
    SCHEDULED = 1
    MOVED = 2

    STATUS = (
        (SCHEDULED, "DON'T CHANGED TIME"),
        (MOVED, 'CHANGE TIME')
    )

    tittle = models.CharField(max_length=60)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_status = models.IntegerField(choices=STATUS, default=SCHEDULED)
    time_for_moved = models.DateTimeField(blank=True, null=True)
    # lesson_status = models.IntegerField(choices=STATUS)


class TimeTable(models.Model):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

    WEEK_DAYS = (
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    )

    first_day = models.IntegerField(choices=WEEK_DAYS)
    first_day_time = models.TimeField()
    second_day = models.IntegerField(choices=WEEK_DAYS)
    second_day_time = models.TimeField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)