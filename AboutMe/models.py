from django.db import models

# Create your models here.
class AboutMe(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='AboutMe/images')
    url = models.URLField(blank=True)

    def __str__(self):  # this will display the project name (title) under admin section
        return self.title
