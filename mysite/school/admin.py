from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import Student, Lecturer, Lesson, Course, CustomUser, TimeTable
from .forms import CustomUserChangeForm, CustomUserCreationForm


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'full_name'
    list_display_links = 'full_name',


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'id', 'tittle', 'lecturer', 'course'
    list_display_links = 'tittle',


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1


class TimeTableInline(admin.TabularInline):
    model = TimeTable
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    list_display_links = 'name',
    inlines = (LessonInline, TimeTableInline)


@admin.register(Lecturer)
class LecturerAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'full_name',
    list_display_links = 'full_name',
    # inlines = (LessonInline, LecturerInline)


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = 'email', 'username',
#     list_display_links = 'username',
#
#
# admin.site.register(CustomUser, CustomUserAdmin)
