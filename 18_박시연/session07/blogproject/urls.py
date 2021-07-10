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
from os import stat
from django.contrib import admin
from django.urls import path

# blog app에서 views를 불러와 별칭 b로 저장한다.
from blog import views as b
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # home 화면 연결, b에서 home이라는 함수를 불러와 name home으로 저장한다.
    path('', b.home, name='home'),
    path('cat', b.cat, name='cat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
