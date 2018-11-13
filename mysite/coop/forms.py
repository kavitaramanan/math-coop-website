from django.forms import ModelForm
from coop.models import Outreach, Person

class OutreachForm(ModelForm):
    class Meta:
        model = Outreach
        exclude = []

class PersonForm(ModelForm):
    class Meta:
        model = Person
        exclude = []