from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the StuHom index.")

from .models import Student, Homework

from django.views.generic.edit import CreateView

class HomeworkCreate(CreateView):
    model = Homework
    template_name = 'homework_form.html'
    fields = ['commit_date','headline','attach','remark', 'student']