"""personal_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('',views.home,name='home'),
    path('aboutme', include('AboutMe.urls')),
    path('message',views.message,name='message'),
    path('',views.check, name='check'),
    path('send',views.mailfunc,name='send'),
    path('skillbar',views.skillbar,name='skillbar'),
    path('skillbarTools',views.skillbarTools,name='skillbarTools'),
    path('skillbarFrameworks',views.skillbarFrameworks,name='skillbarFrameworks'),
    path('resume',views.resume,name='resume'),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)