from django.contrib import admin
from .models import Article

# Make articles viewable on Django admin/ page
admin.site.register(Article)
