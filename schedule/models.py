from django.db import models
from django.contrib.auth.models import User

class SchedulePost(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='schedule_image')
    course_name = models.CharField(max_length=200)
    modules_taken = models.CharField(max_length=500)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
