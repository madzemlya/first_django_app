from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Lecturer, Course, Lesson


def index_view(request):
    course = Course.objects.get(pk=1)
    all_lessons = Lesson.objects.all()
    print(all_lessons)
    context = {
        'foo': 'bar',
        'spam': 'eggs',
        'article': course,
        'all_lessons': all_lessons,
        # 'all_articles': Article.objects.all(),
        # 'all_j_authors': Author.objects.filter(first_name__startswith='J')
    }
    return render(request, 'mysite/index.html', context=context)