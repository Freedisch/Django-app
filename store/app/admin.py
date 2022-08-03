from django.contrib import admin
from .models import *
# Register your models here.
class InstructorAdmin(admin.ModelAdmin):
    fields = ['first_name','full_time']

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
    
class CourseAdmin(admin.ModelAdmin):
    fields = ['name', 'description']
    inlines = [LessonInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Instructor, InstructorAdmin)
