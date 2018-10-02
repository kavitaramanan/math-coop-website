from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField("Topic", max_length=50)

class Presentation(models.Model):
    name = models.CharField("Name", max_length=200)
    file_dir = models.CharField("Presentation", max_length=200)
    summary = models.CharField("Summary", max_length=1000)
    author = models.CharField("Author", max_length=50)

class PresentationTopic(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

class PresentationFile(models.Model):
    specifications = models.FileField(upload_to='ppts/')
    pres = models.ForeignKey(Presentation, on_delete=models.CASCADE)

