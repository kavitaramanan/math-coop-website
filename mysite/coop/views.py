from django.shortcuts import render, HttpResponse
from .models import Presentation, PresentationFile, PresentationTopic, Topic

import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    return render(request, 'coop/base.html')

def management(request):
    context = {"presentations": []} 
    presentations = Presentation.objects.all()
    for pres in presentations:
        context["presentations"].append({
            "name": pres.name,
            "summary": pres.summary,
            "author": pres.author,
            "topics": topics(pres)
        })
    logger.warning(context)
    return  render(request, 'coop/manage.html', context)

def upload(request):
    if request.method == "GET":
        return render(request, 'coop/upload.html')

def topics(pres):
    pres_topics = list(PresentationTopic.objects.filter(presentation=pres.pk))
    try:
        response = pres_topics.pop().topic.name
    except:
        response = ""

    if response:
        for comb in pres_topics:
            response += ", " + comb.topic.name
    
    return response
