from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from app.models import *
def display_Topic(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_Topic.html',d)
def display_webpages(request):
    LWO=Webpages.objects.all()
    LWO=Webpages.objects.filter(name__startswith='m')
    LWO=Webpages.objects.filter(name__contains='e')
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(date__year__gt='2000')
    LAO=AccessRecords.objects.filter(date__year__lt='2000')
    LAO=AccessRecords.objects.filter(date__month='10')
    LAO=AccessRecords.objects.filter(date__day='26')
    LAO=AccessRecords.objects.filter(date__year='1970')
    LAO=AccessRecords.objects.all()
    LAO=AccessRecords.objects.filter(Q(date__year='2001')&Q(date__month='10'))
    LAO=AccessRecords.objects.filter(Q(date__year='1970')|Q(date__month='10'))

    d={'LAO':LAO}
    return render(request,'display_accessrecords.html',d)

