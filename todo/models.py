from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title