from django.contrib import admin

# Register your models here.
# students/admin.py

from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'roll')
    search_fields = ('name', 'city')

