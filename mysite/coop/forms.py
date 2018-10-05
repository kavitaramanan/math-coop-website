from django.forms import ModelForm
from coop.models import Outreach

class OutreachForm(ModelForm):
    class Meta:
        model = Outreach
        exclude = []