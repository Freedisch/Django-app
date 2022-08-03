from django.test import TestCase

# Create your tests here.
from django.contrib import admin
from .models import *
# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    fields = ['user','full_time']

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
    
class CourseAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'name', 'description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
