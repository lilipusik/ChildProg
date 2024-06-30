from django.contrib import admin
from school.models import Courses, CoursesTheory, PracticeTasks, Reviews, Like
from django.utils.translation import gettext_lazy as _

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)
    fieldsets = (
        (_('Основная информация'), {'fields': ('name', 'description', 'image')}),
    )

@admin.register(CoursesTheory)
class CoursesTheoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'course')
    search_fields = ('title', 'course__name')
    list_filter = ('course',)
    fieldsets = (
        (_('Основная информация'), {'fields': ('course', 'title', 'theory')}),
    )

@admin.register(PracticeTasks)
class PracticeTasksAdmin(admin.ModelAdmin):
    list_display = ('theory', 'description', 'difficulty')
    search_fields = ('theory__title', 'description')
    list_filter = ('theory', 'difficulty')
    fieldsets = (
        (_('Основная информация'), {'fields': ('theory', 'description', 'difficulty', 'answer')}),
    )

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'review', 'create_date')
    search_fields = ('user__username', 'review')
    list_filter = ('rating', 'create_date')
    fieldsets = (
        (_('Основная информация'), {'fields': ('user', 'rating', 'review')}),
        (_('Дата создания'), {'fields': ('create_date',)}),
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'created_at')
    search_fields = ('user__username', 'course__name')
    list_filter = ('created_at',)
    fieldsets = (
        (_('Основная информация'), {'fields': ('user', 'course')}),
        (_('Дата создания'), {'fields': ('created_at',)}),
    )
