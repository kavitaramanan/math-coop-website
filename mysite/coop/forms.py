from django import forms
from coop.models import Outreach, Person

class OutreachForm(forms.ModelForm):
    class Meta:
        model = Outreach
        exclude = []

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = []
