"""catproject URL Configuration

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
from cat import views as b
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',b.home, name="home"),
    path('<str:id>', b.detail, name='detail'),
    # path('new/', b.new, name='new'),
    # path('create/', b.create, name='create'),
    path('post/', b.make_post, name='post'),
    # path('edit/<str:id>', b.edit, name='edit'),
    path('update/<str:id>', b.update, name='update'),
    path('delete/<str:id>', b.delete, name='delete'),
    # comment
    path('create_comment/<int:cat_id>', b.create_comment, name="create_comment"),
    path('delete_comment/<int:cat_id>/<int:comment_id>/', b.delete_comment, name="delete_comment"),
    path('update_comment/<int:cat_id>/<int:comment_id>/', b.update_comment, name="update_comment")
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)