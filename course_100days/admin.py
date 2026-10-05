from django.contrib import admin
from .models import Challenge, StudySession


@admin.register(StudySession)
class StudySessionAdmin(admin.ModelAdmin):
    list_display = ["owner", "clockin_time", "clockout_time", "duration_display"]
    list_filter = ["owner"]


@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ["owner", "start_date"]
