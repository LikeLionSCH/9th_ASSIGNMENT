"""myproject URL Configuration

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
# from firstapp import views as first
# from wordCount import views as wc
from CountApp import views as cnt
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', first.welcome, name='welcome'),
    # path('hello/', first.hello, name='hello'),
    # path('wc/', wc.home, name='wc'),
    # path('wc/result/', wc.result, name='result'),
    path('count/', cnt.count, name='count'),
    path('test/', cnt.test, name='test'),
    path('count/results/', cnt.results, name='results'),
    path('test/test1/', cnt.test1, name='test1'),
    path('test/test2/', cnt.test2, name='test2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)