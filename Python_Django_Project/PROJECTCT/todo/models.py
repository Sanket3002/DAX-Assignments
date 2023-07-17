from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(blank=True, null=True)
    task_status = models.BooleanField(null=False,default=False)



    def publish(self):
        self.start_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


    



