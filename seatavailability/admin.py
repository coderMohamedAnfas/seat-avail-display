# seatavailability/admin.py
from django.contrib import admin
from .models import Branch, Category

admin.site.register(Branch)
admin.site.register(Category)
