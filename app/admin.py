from django.contrib import admin
from .models import Category, Klass, Praduct

admin.site.register([Category, Klass, Praduct])