from django.shortcuts import render
from .models import Subject, LectureNote, YoutubeVideo, Blurb
from django.http import HttpResponse
from .forms import uploadNoteForm, createSubjectForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .YTScrapper import YTScrape
from .WikiScrapper import wiki
from django.db import models

sub = Subject.objects.all().first()

def subject(request, subjectStr):
    if subjectStr:
        sub = Subject.objects.get(name__iexact=subjectStr)
    return render(request,"subject.html",{"subject":sub})

def index(request):
    return render(request,'index.html',{"subs":Subject.objects.all})
    


def note(request, noteStr):
    note = LectureNote.objects.get(title__iexact=noteStr)
    return render(request,"note.html",{"note":note})

def upload(request):

    if request.method == "POST":
        form = uploadNoteForm(request.POST, request.FILES, request.user)
        
        if form.is_valid():
            newTitle = form.cleaned_data["title"].replace(" ","_")
            obj = LectureNote(image=form.cleaned_data["image"],subject = form.cleaned_data["subject"],favorites=0,title=newTitle,author=request.user)
            obj.save()
            
            

            return HttpResponseRedirect(reverse(subject, args=[form.cleaned_data["subject"].name.replace(' ','_')]))
        
    else:
        form = uploadNoteForm()

    context = {
        'form':form
    }

    return render(request,"./form.html",context)

def newSubject(request):
    if request.method == "POST":
        form = createSubjectForm(request.POST, request.user)
        
        if form.is_valid():

            obj = Subject(name=form.cleaned_data["name"].replace(" ","_"))
            obj.save()
            
            blurb = Blurb(blurbText=wiki(form.cleaned_data["name"]),fromLink="https://wikipedia.org/",subject=obj)
            blurb.save()

            vidUrls = []

            for video in YTScrape(form.cleaned_data["name"] + "lecture","8"):
                if(video["url"] not in vidUrls):
                    vidUrls.append(video["url"])
                    lec = YoutubeVideo(subject=obj,link=video["url"], favorites=0)
                    lec.save()
            
            for video in YTScrape(form.cleaned_data["name"] + "course","6"):
                if(video["url"] not in vidUrls):
                    vidUrls.append(video["url"])
                    lec = YoutubeVideo(subject=obj,link=video["url"], favorites=0)
                    lec.save()

            return HttpResponseRedirect(reverse(subject, args=[form.cleaned_data['name'].replace(' ','_')]))
        
    else:
        form = createSubjectForm()

    context = {
        'form':form
    }

    return render(request,"./form.html",context)
