from django.db import models
# Create your models here.
class creat_category(models.Model):
    category_name=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.category_name
    # category=models.ManyToManyField(Task)