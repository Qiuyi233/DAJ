分布式作业——建立学生作业上传系统的实验报告

### 第一步：建立一个App
进入mysite路径，在该路径下建立App StuHom
```
python manage.py startapp StuHom
```

### 第二步：建立一个视图
```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the StuHom index.")
```

### 第三步：将视图映射到 URL
在StuHom目录下建立一个 urls.py,放入代码：
```
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
```

将根 URLconf 指向模块

```
urlpatterns = [
    path('StuHom/', include('StuHom.urls')),
    path('admin/', admin.site.urls),
]
```

**在命令行中输入 *python manage.py runserver***
**可以在  *http://localhost:8000/StuHom/*  中看到  *Hello, world. You're at the StuHom index.* 的提示**

### 第四步：进行数据库设置
```
python manage.py migrate
```

### 第五步：创建模型
进入 moedels.py

```
from django.db import models

 class Student(models.Model):
    full_name = models.CharField(max_length=70)
    #age = models.IntegerField()
    class Sex(models.IntegerChoices):
        MALE = 1, '男'
        FEMALE = 2, '女'
        OTHER = 3, '其他'

    sex = models.IntegerField(choices=Sex.choices)

    def __str__(self):
        return self.full_name

class Homework(models.Model):
    commit_date = models.DateField()
    headline = models.CharField(max_length=200)
    attach = models.FileField()
    remark = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```

### 第六步：激活模型
在文件 mysite/settings.py 中 INSTALLED_APPS 子项添加点式路径
运行 makemigrations 命令，Django 会检测你对模型文件的修改（在这种情况下，你已经取得了新的），并且把修改的部分储存为一次 迁移。

### 第七步：进入数据库后台
输入 
```
python manage.py runserver
```
 进入 *http://localhost:8000/admin/StuHom*

进入 *http://localhost:8000/admin/StuHom/student/* Add一个学生

进入*http://localhost:8000/admin/StuHom/homework/*Add一项作业

### 第八步：进入数据库查看自己所提交的作业

```
sqlite
.open db.sqlite3
.tables
select * from StuHom_student;
select * from StuHom_homework;
```
可以看到自己的提交结果。

### 第九步：创建新的视图

创建templates目录，再创建StuHom目录，再此目录下建立homework_form.html

添加代码：
```
<html>
<body>
<form method="post" enctype="multipart/form-data" >{% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Save">
</form>
</body>
</html>
```
建立base.html,添加代码：
```
{% load static %}
<html>
<head>
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
    <img src="{% static 'images/sitelogo.png' %}" alt="Logo">
    {% block content %}{% endblock %}
</body>
</html>
```

### 第十步：建立upload上传路径
在StuHom/urls.py中添加path：
```
path('upload', views.HomeworkCreate.as_view()),
```
### 第十一步：进入网页查看
进入网页：*http://localhost:8000/StuHom/upload*
可以看到文件上传提交的界面。

**文件上传功能实现完成**