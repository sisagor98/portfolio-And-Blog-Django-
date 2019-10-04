from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
