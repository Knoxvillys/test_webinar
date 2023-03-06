from django.contrib import admin

from .models import Video, Teacher, Сourse
# Register your models here.

admin.site.register(Teacher)
admin.site.register(Сourse)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    filter_horizontal = ['teacher'] # виджет для фильтрации преподавателей.
    #filter_vertical = ['teacher'] # виджет для фильтрации преподавателей.
