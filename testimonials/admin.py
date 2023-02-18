from django.contrib import admin
from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'review', 'approved')
    list_filter = ('approved',)
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
