from django.urls import path, re_path
from . import views

app_name = 'bugs'

urlpatterns = [
    path('', views.bugs, name="bugs"),
    path('create/', views.create, name="create"),
    re_path(r'(?P<slug>[\w-]+)/$', views.bug_detail, name="detail"),
]