from django.db import models
# models is basically a class which will be working with dB
# Create your models here.
# inherited models class
class Project(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    image=models.ImageField(upload_to='portfolio/images')
    url=models.URLField(blank=True)


    def __str__(self):  # this will display the project name (title) under admin section
        return self.title

