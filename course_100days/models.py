from django.db import models
from django.conf import settings


class StudySession(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="study_sessions",)
    clockin_time = models.DateTimeField()
    clockout_time = models.DateTimeField()
    learning = models.CharField(max_length=500, blank=True)
    
    
    class Meta:
        ordering = ['-clockin_time']

    def __str__(self):
        start = self.clockin_time.strftime("%Y-%m-%d %H:%M")
        if self.clockout_time:
            end = self.clockout_time.strftime("%Y-%m-%d %H:%M")
            return f"Study Session: {start} - {end}"
        return f"{start} - (in progress)"
    

    @property
    def duration(self):
        return self.clockout_time - self.clockin_time
    
    
    @property
    def duration_display(self):
        total_minutes = int(self.duration.total_seconds() // 60)
        hours, minutes = divmod(total_minutes, 60)
        if hours:
            return f"{hours}h {minutes:02d}m"
        return f"{minutes}m"
    
    
class Challenge(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="challenge",
    )
    start_date = models.DateField()

    def __str__(self):
        return f"{self.owner} started on {self.start_date}"
