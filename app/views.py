from django.shortcuts import render

# Create your views here.
from app.models import *

def display_Topics(request):
    TO=Topic.objects.all()
    d={'TopicS':TO}
    return render(request,'display_Topics.html',d)


def display_Webpages(request):
    WO=Webpages.objects.all()
    d={'webpages':WO}
    return render(request,'display_Webpages.html',d)