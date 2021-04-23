from django.contrib import admin
from .models import Bugs

# Make articles viewable on Django admin/ page
admin.site.register(Bugs)