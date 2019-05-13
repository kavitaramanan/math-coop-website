from django.db import models

# Create your models here.
class Presentation(models.Model):
    name = models.CharField("Name", max_length=200)
    summary = models.CharField("Summary", max_length=1000, blank=True, default="", null=True)
    author = models.CharField("Author", max_length=50, blank=True, default="", null=True)
    level = models.CharField("Level", max_length=200, blank=True, default="", null=True)
    topics = models.CharField("Topic", max_length=200, blank=True, default="", null=True)

    def __str__(self):
        return self.name


class File(models.Model):
    pres = models.ForeignKey(Presentation, on_delete=models.CASCADE)
    f = models.FileField(upload_to='')
    name = models.CharField("Name", max_length=75, blank=True, default=None, null=True)
    
    def __str__(self):
        return self.name if self.name else self.f.name

class Person(models.Model):
    name = models.CharField("Name", max_length=50)
    image = models.ImageField(upload_to="images/", blank=True, default="", null=True)
    bio = models.CharField("Biography", max_length=1000, blank=True, default="", null=True)
    STATUS_CHOICES = (
            ("faculty", "Faculty Adivsor"),
            ("member", "Current Member"),
            ("alumni", "Alumni")
        )
    status = models.CharField("status", max_length=7, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "People"

class Outreach(models.Model):
    name = models.CharField("Name", max_length=100)
    location = models.CharField("Location", max_length=200, blank=True, default="", null=True)
    date = models.DateField("Date", blank=True, default="", null=True)
    description = models.CharField("Description", max_length=1000, blank=True, default="", null=True)
    people = models.ManyToManyField(Person, related_name="outreach", blank=True, default="", null=True)
    
    def __str__(self):
        return self.name
