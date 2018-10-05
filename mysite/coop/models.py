from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField("Topic", max_length=50)

class Presentation(models.Model):
    name = models.CharField("Name", max_length=200)
    f = models.FileField(upload_to='ppts/')
    summary = models.CharField("Summary", max_length=1000)
    author = models.CharField("Author", max_length=50)

class PresentationTopic(models.Model):
    presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
