from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Presentation, Topic, Outreach, Person, File
from .forms import OutreachForm, PersonForm
from django.conf import settings
from PIL import Image

import os
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, 'coop/base.html')

def people(request):
    people = Person.objects.all()
    return render(request, 'coop/people.html', {"people": people})

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
            "topics": get_topics(pres)
        })
    print(context)
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
    return render(request, 'coop/outreach.html', context)


def download(request):
    file_name = request.GET.get("file_name")
    file_path = settings.MEDIA_ROOT +'\\'+ file_name
    print("here")
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            print("opened successfully")
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

def get_topics(pres):
    topics = pres.topics.all()
    response = ""
    for topic in topics:
        response += topic.name + ", "

    return response[:-2] # remove trailing comma

def get_people(outreach):
    people = outreach.people.all()
    return people # remove trailing comma

def get_files(pres):
    files = list(File.objects.filter(pres=pres.pk))
    try:
        response = [files.pop().f.name]
    except:
        response = ""

    if response:
        for f in files:
            response.append(f.f.name)
    
    return response