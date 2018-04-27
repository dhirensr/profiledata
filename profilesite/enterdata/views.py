from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.template import loader
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from django.views import generic
from .forms import NameForm
from .models import EnterData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def enterdata(request):
    if request.method =='POST':
        form = NameForm(request.POST)
        if form.is_valid():
            work_exp = form.cleaned_data["work_exp"]
            german_grade = form.cleaned_data["german_grade"]
            bachelors_percent = form.cleaned_data["bachelors_percent"]
            EnterData.objects.create(work_exp = work_exp,german_grade = german_grade,\
                                     bachelors_percent =bachelors_percent)
            return HttpResponseRedirect('/enterdata/')
    else:
        form=NameForm()
    return render(request,'enterdata/name.html',{'form' : form})

def viewdata(request):
    if request.method =='GET':
        all_objs=EnterData.objects.all()
        paginator = Paginator(all_objs, 2)
        page = request.GET.get('page')
        profiles = paginator.get_page(page)
        return render(request,'enterdata/profiles.html',{'profiles' : profiles})


def viewprofile(request,profile_id):
    if request.method =='GET':
        profile=EnterData.objects.get(pk=profile_id)
        return render(request,'enterdata/profile.html',{'profile' : profile})
