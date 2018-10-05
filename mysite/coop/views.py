from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Presentation, PresentationTopic, Topic

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
        context = {"topics": Topic.objects.all()}
        return render(request, 'coop/upload.html', context)
    elif request.method == "POST":
        pres = Presentation()
        pres.name = request.POST.get("nameInput", "")
        pres.f = request.FILES
        pres.summary = request.POST.get("summaryInput", "")
        pres.author = request.POST.get("authorInput", "")
        pres.save()
        topics = request.POST.getlist("topicInput", [])
        for topic in topics:
            topic = Topic.objects.get(pk=topic)
            pt = PresentationTopic()
            pt.presentation = pres
            pt.topic = topic
            pt.save()
        return redirect(reverse("manage"))

def outreach(request):
    context = {
        "outreach_history": [
            {"location": "Brown University", "date": "09/25/2018", "description": ";afihpeorfnlvdjknf;kjnaes;dfkjcn"},
            {"location": "Brown University", "date": "09/26/2018", "description": ";afihpeorfnlvdjknf;kjnaes;dfkjcn"},
            {"location": "Brown University", "date": "09/27/2018", "description": ";afihpeorfnlvdjknf;kjnaes;dfkjcn"},
            {"location": "Brown University", "date": "09/28/2018", "description": ";afihpeorfnlvdjknf;kjnaes;dfkjcn"}
        ]
    }
    return render(request, 'coop/outreach.html', context)

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
