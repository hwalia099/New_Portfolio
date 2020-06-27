
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
app_name='AboutMe'
urlpatterns = [

    path('',views.aboutMe,name='aboutmehome'),
    path('<int:aboutme_id>/',views.detail,name='detail')

]