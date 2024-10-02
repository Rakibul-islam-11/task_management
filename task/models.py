from django.db import models
# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=50)
    taskDescription=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)
    date=models.DateField()
    def __str__(self) -> str:
        return self.title