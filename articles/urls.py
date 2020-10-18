from django.urls import path
from . import views
from django.urls import path, re_path

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),
    re_path('(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
