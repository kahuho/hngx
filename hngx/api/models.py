from django.db import models

class StageOneData(models.Model):
    slack_name = models.CharField(max_length=100)
    current_day = models.CharField(max_length=20)
    utc_time = models.DateTimeField()
    track = models.CharField(max_length=20)
    github_file_url = models.URLField()
    github_repo_url = models.URLField()
