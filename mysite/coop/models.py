from django.db import models

# Create your models here.
class Topic(models.Model):
    name = models.CharField("Topic", max_length=50, primary_key=True)

class Presentation(models.Model):
    name = models.CharField("Name", max_length=200, primary_key=True)
    summary = models.CharField("Summary", max_length=1000)
    author = models.CharField("Author", max_length=50)
    level = models.CharField("Level", max_length=200)
    topics = models.ManyToManyField(Topic, related_name="pres")

class File(models.Model):
    pres = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    f = models.FileField(upload_to='ppts/')

class Person(models.Model):
    name = models.CharField("Name", max_length=50, primary_key=True)
    image = models.ImageField(upload_to="images/")
    bio = models.CharField("Biography", max_length=1000)
    class Meta:
        verbose_name_plural = "People"

class Outreach(models.Model):
    name = models.CharField("Name", max_length=100, primary_key=True)
    location = models.CharField("Location", max_length=200)
    date = models.DateField("Date")
    description = models.CharField("Description", max_length=1000)
    people = models.ManyToManyField(Person, related_name="outreach")

# class PersonOutreach(models.Model):
#     person = models.ForeignKey(Person, on_delete=models.CASCADE)
#     outreach = models.ForeignKey(Outreach, on_delete=models.CASCADE)

# class PresentationTopic(models.Model):
#     presentation = models.ForeignKey(Presentation, on_delete=models.CASCADE)
#     topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
 