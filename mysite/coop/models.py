from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField("Topic", max_length=50)

class Presentation(models.Model):
    name = models.CharField("Name", max_length=200)
    summary = models.CharField("Summary", max_length=1000, blank=True, default=None, null=True)
    author = models.CharField("Author", max_length=50, blank=True, default=None, null=True)
    level = models.CharField("Level", max_length=200, blank=True, default=None, null=True)
    topics = models.ManyToManyField(Topic, related_name="pres", blank=True, default=None, null=True)

class File(models.Model):
    pres = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    f = models.FileField(upload_to='ppts/')

class Person(models.Model):
    name = models.CharField("Name", max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, default=None, null=True)
    bio = models.CharField("Biography", max_length=1000, blank=True, default=None, null=True)
    class Meta:
        verbose_name_plural = "People"

class Outreach(models.Model):
    name = models.CharField("Name", max_length=100)
    location = models.CharField("Location", max_length=200, blank=True, default=None, null=True)
    date = models.DateField("Date", blank=True, default=None, null=True)
    description = models.CharField("Description", max_length=1000, blank=True, default=None, null=True)
    people = models.ManyToManyField(Person, related_name="outreach", blank=True, default=None, null=True)
 