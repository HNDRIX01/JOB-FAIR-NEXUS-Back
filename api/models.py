from django.db import models

class UserProfile(models.Model):
    study = models.CharField(max_length=255, help_text="Field of study")
    hobby = models.CharField(max_length=255, help_text="User's hobby")
    skill = models.CharField(max_length=255, help_text="User's skill")
    job = models.CharField(max_length=255, help_text="Dream job")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp of the profile creation")

    def __str__(self):
        return f"{self.study} | {self.job}"


