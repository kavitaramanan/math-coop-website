from django.shortcuts import render, HttpResponse, redirect, reverse
from .models import Presentation, PresentationTopic, Topic, Outreach, Person, PersonOutreach, File
from .forms import OutreachForm, PersonForm
from PIL import Image

import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
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
    return render(request, 'coop/base.html', context)

def people(request):
    people = Person.objects.all()
    return render(request, 'coop/people.html', {"people": people})

def pres(request):
    pres = Presentation.objects.all()
    return render(request, 'coop/pres.html', {"presentations": pres})

def outreach(request):
    context = {"outreach_history": Outreach.objects.all()}
    return render(request, 'coop/outreach.html', context)

def manage(request):
    return render(request, 'coop/manage/base.html')

def manage_pres(request):
    context = {"presentations": []} 
    presentations = Presentation.objects.all()
    for pres in presentations:
        context["presentations"].append({
            "name": pres.name,
            "summary": pres.summary,
            "author": pres.author,
            "level": pres.level,
            "topics": get_topics(pres)
        })
    return  render(request, 'coop/manage/pres.html', context)

def upload_pres(request):
    if request.method == "GET":
        context = {"topics": Topic.objects.all()}
        return render(request, 'coop/manage/upload/pres.html', context)
    elif request.method == "POST":
        pres = Presentation()
        # set attributes
        attrInputs = ["summaryInput", "authorInput", "levelInput", "nameInput"]
        attrs = ["summary", "author", "level", "name"]
        for attrInput in attrInputs:
            new_value = request.POST.get(attrInput, default="")
            setattr(pres, attrs.pop(0), new_value)
        pres.save()

        topic_str = request.POST.get("topicInput", "")
        topic_list = topic_str.split(", ")        
        for topic_name in topic_list:
            # get topic object if it exists otherwise create it
            try:
                topic = Topic.objects.filter(name=topic_name)[0]
            except:
                topic = Topic()
                topic.name = topic_name
                topic.save()
            pt = PresentationTopic()
            pt.presentation = pres
            pt.topic = topic
            pt.save()

        files = request.FILES.getlist("fileInput")
        for f in files:
            new_f = File()
            new_f.pres = pres
            new_f.f = f
            new_f.save()
        return redirect(reverse("manage_pres"))

def edit_pres(request):
    def update_topics(topic_list):
        # delete old topics and remove them from the list
        current_pres_topic_list = PresentationTopic.objects.filter(presentation=pres)
        for pres_topic in current_pres_topic_list:
            topic_name = pres_topic.topic.name
            logger.warning(topic_name)
            if topic_name not in topic_list: pres_topic.delete()
            else: topic_list.remove(topic_name)
        # create new pres topic pairs
        for topic_name in topic_list:
            logger.warning(topic_name)
            # get topic object if it exists otherwise create it
            topic = Topic.objects.filter(name=topic_name)
            if not topic:
                topic = Topic()
                topic.name = topic_name
                topic.save()    
            pt = PresentationTopic()
            pt.presentation = pres
            pt.topic = topic
            pt.save()

    if request.method == "GET":
        pres = request.GET.get("pres")
        pres = Presentation.objects.get(name=pres)
        topics = get_topics(pres)
        return render(request, "coop/manage/edit/pres.html", {"pres": pres, "topics": topics})

    elif request.method == "POST":
        pres = request.POST.get("pres")
        pres = Presentation.objects.filter(name=pres)[0]
        
        # update attributes
        attrInputs = ["summaryInput", "authorInput", "levelInput", "nameInput"]
        attrs = ["summary", "author", "level", "name"]
        print(request.POST)
        for i, attrInput in enumerate(attrInputs):
            new_value = request.POST.get(attrInput, default="")
            print(attrs[i], new_value)
            setattr(pres, attrs[i], new_value)
        pres.save()
        
        # update topics
        # get and format topic names
        topic_str = request.POST.get("topicInput", "")
        topic_list = topic_str.split(", ")
        update_topics(topic_list)

        # add new files
        files = request.FILES.getlist("fileInput")
        for f in files:
            new_f = File()
            new_f.pres = pres
            new_f.f = f
            new_f.save()

        return redirect(reverse("manage_pres"))

def manage_outreach(request):
    context = {"outreachs": []} 
    outreachs = Outreach.objects.all()
    for outreach in outreachs:
        context["outreachs"].append({
            "name": outreach.name,
            "location": outreach.location,
            "date": outreach.date,
            "description": outreach.description,
            "people": get_people(outreach)
        })
    return  render(request, 'coop/manage/outreach.html', context)

def upload_outreach(request):
    if request.method == "GET":
        form = OutreachForm()
        return render(request, 'coop/manage/upload/outreach.html', {"form": form})
    else:
        form = OutreachForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("invalid" + str(form))
        return redirect(reverse('manage_outreach'))

def manage_people(request):
    context = {"people": []} 
    people = Person.objects.all()
    for person in people:
        context["people"].append({
            "name": person.name,
            "bio": person.bio,
            "image": person.image,
            "outreachs": get_outreach(person)
        })
    return  render(request, 'coop/manage/people.html', context)

def add_person(request):
    if request.method == "GET":
        form = PersonForm()
        return render(request, 'coop/manage/upload/person.html', {"form": form})
    else:
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(reverse('manage_people'))

def manage_topics(request):
    context = {"topics": []}   
    topics = Topic.objects.all()
    for person in topics:
        context["topics"].append({"name": person.name})
    return  render(request, 'coop/manage/topics.html', context)

def upload_topic(request):
    name = request.GET.get("name")
    topic = Topic()
    topic.name = name
    topic.save()
    return HttpResponse("Success")

def delete(request):
    classDict = {
        "pres": Presentation,
        "person": Person,
        "topic": Topic,
        "outreach": Outreach,
    }
    obj_type = request.GET.get("obj")
    obj_name = request.GET.get("name")
    classDict[obj_type].objects.get(name=obj_name).delete()
    return HttpResponse("Success")

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
    pres_topics = list(PresentationTopic.objects.filter(presentation=pres.pk))
    try:
        response = pres_topics.pop().topic.name
    except:
        response = ""

    if response:
        for comb in pres_topics:
            response += ", " + comb.topic.name
    
    return response

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