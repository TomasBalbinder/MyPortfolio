from django.db import models


# Create your models here.


class Blog(models.Model):
    

    title = models.CharField(max_length=40)
    date = models.DateField()
    text = models.TextField(max_length=1000)


    def __str__(self):
        return str(self.id) + "." + self.title
