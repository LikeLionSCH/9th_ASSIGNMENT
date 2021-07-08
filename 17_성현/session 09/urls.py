"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views as b


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', b.home, name="home"),
    path('education/', b.education, name="education"),
    path('edu_detail/', b.edu_detail, name="edu_detail"),
    path('community/', b.community, name="community"),
    path('community2/', b.community2, name="community2"),
    path('write/', b.write, name="write"),
    path('login/', b.login, name="login"),
    path('view/', b.view, name="view"),
    path('edit/', b.edit, name="edit"),
    path('first/', b.first, name="first"),
    path('second/', b.second, name="second"),
    path('answer/<int:ids>', b.answer, name="answer"),
    path('create_comment/<int:blog_id>', b.create_comment, name="create_comment"),
    path('create_comment2/<int:blog_id>', b.create_comment2, name="create_comment2"),
    path('update_comment/<int:blog_id>/<int:comment_id>', b.update_comment, name="update_comment"),
    path('update_comment2/<int:blog_id>/<int:comment_id>', b.update_comment2, name="update_comment2"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
