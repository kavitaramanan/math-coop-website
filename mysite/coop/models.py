from django.db import models

# Create your models here.
class PresentationFile(models.Model):
    specifications = models.FileField(upload_to='ppts/')
    name = models.CharField(max_length=200)

class Presentation(models.Model):
    name = models.CharField("Name", max_length=200)
    file_dir = models.CharField("File", max_length=200)
    summary = models.CharField("Summary", max_length=1000)
    author = models.CharField("Author", max_length=50)
    topics = models.CharField("Topics", max_length = 200)


class Topic(models.Model):
    name = models.CharField("Topic", max_length=50)