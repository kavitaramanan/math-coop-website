from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Presentation, Outreach, Person, File
from .forms import OutreachForm, PersonForm, ContactForm
from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from PIL import Image

import os
import logging
from datetime import date

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, 'coop/base2.html')

def people(request):
    faculty = Person.objects.all().filter(status='faculty')
    members = Person.objects.all().filter(status='member')
    alumni = Person.objects.all().filter(status='alumni')
    return render(request, 'coop/people.html', 
        {'faculty': faculty, 'members': members, 'alumni': alumni})

def pres(request):    
    context = {"presentations": []} 
    presentations = Presentation.objects.all()
    for pres in presentations:
        context["presentations"].append({
            "name": pres.name,
            "summary": pres.summary,
            "author": pres.author,
            "level": pres.level,
            "files": get_files(pres),
            "topics": pres.topics
        })
    return render(request, 'coop/pres.html', context)

def outreach(request):
    context = {"outreach_history": []} 
    outreach = Outreach.objects.all()
    for out in outreach:
        context["outreach_history"].append({
            "name": out.name,
            "location": out.location,
            "date": out.date,
            "description": out.description,
            "people": get_people(out)
        })
    context["outreach_history"] = sorted(context["outreach_history"], key=lambda k: (k['date'] if k['date'] else date.min), reverse=True)
    return render(request, 'coop/outreach.html', context)

def download(request):
    file_name = request.GET.get("file_name")
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

def contact(request):
    """Page to allow users to contact the mathcoop"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['tottaway123@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('index')
    return render(request, 'coop/contact.html', {'form': form})
    

#def get_topics(pres):
#    topics = pres.topics.all()
#    response = ""
#    for topic in topics:
#        response += topic.name + ", "
#
#    return response[:-2] # remove trailing comma

def get_people(outreach):
    people = outreach.people.all()
    return people # remove trailing comma

def get_files(pres):
    files = list(File.objects.filter(pres=pres.pk))
    try:
        response = [files.pop()]
    except:
        response = ""

    if response:
        for f in files:
            response.append(f)
    
    return response
