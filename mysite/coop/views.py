from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Presentation, Topic, Outreach, Person, File
from .forms import OutreachForm, PersonForm
from PIL import Image

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
    context = {"outreach_history": Outreach.objects.all()}
    return render(request, 'coop/outreach.html', context)


def download(request, file_name):
    file_path = settings.MEDIA_ROOT +'/ppts'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str(file_name) 
    return response

def get_topics(pres):
    topics = pres.topics.all()
    response = ""
    for topic in topics:
        response += topic.name + ", "

    return response[:-2] # remove trailing comma

def get_outreach(person):
    person_outreachs = list(PersonOutreach.objects.filter(person=person.pk))
    try:
        response = [person_outreachs.pop().topic]
    except:
        response = ""

    if response:
        for pair in person_outreachs:
            response.append(pair.outreach)
    
    return response

def get_people(outreach):
    person_outreachs = list(PersonOutreach.objects.filter(outreach=outreach.pk))
    try:
        response = [person_outreachs.pop().topic]
    except:
        response = ""

    if response:
        for pair in person_outreachs:
            response.append(pair.outreach)
    
    return response

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