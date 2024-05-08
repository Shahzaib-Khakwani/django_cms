from django.contrib import admin

from .models import Subject, Course, Module 
# Register your models here.

@admin.register(Subject)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

class ModuleInline(admin.StackedInline):
    model = Module


@admin.register(Course)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'created', 'subject']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overeview']
    inline = [ModuleInline]
