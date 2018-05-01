from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.template import loader
from django.utils import timezone
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.urls import reverse
from django.views import generic
from .forms import NameForm,TestForm
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
        paginator = Paginator(all_objs, 5)
        page = request.GET.get('page')
        profiles = paginator.get_page(page)
        return render(request,'enterdata/profiles.html',{'profiles' : profiles})


def viewprofile(request,profile_id):
    if request.method =='GET':
        profile=EnterData.objects.get(pk=profile_id)
        return render(request,'enterdata/profile.html',{'profile' : profile})


def testdata(request):
    if request.method =='POST':
        form = TestForm(request.POST)
        if form.is_valid():
            hint1 = form.cleaned_data["hint1"]
            hint2 = form.cleaned_data["hint2"]
            hint3 = form.cleaned_data["hint3"]
            hints= [hint1,hint2,hint3]
            # german_grade = form.cleaned_data["german_grade"]
            # bachelors_percent = form.cleaned_data["bachelors_percent"]
            EnterData.objects.create(work_exp = "1",german_grade = "a2",\
                                     hints=hints)
            return HttpResponseRedirect('/admin/enterdata/enterdata')
    else:
        form=TestForm()
    return render(request,'enterdata/name.html',{'form' : form})


def testdataedit(request,object_id):
    obj= EnterData.objects.get(pk=object_id)
    form=TestForm(request.POST)
    if request.method =='GET':
        form=TestForm({'work_exp' : obj.work_exp,'first_name':obj.first_name,\
                       'hint1' : obj.hints[0],'hint2' : obj.hints[1],\
                       'hint3': obj.hints[2]})
            # german_grade = form.cleaned_data["german_grade"]
            # bachelors_percent = form.cleaned_data["bachelors_percent"]
        return render(request,'enterdata/edit.html',{'form' : form,
                                                     'object_id' : object_id})
    else:
        if form.is_valid():
            hint1 = form.cleaned_data["hint1"]
            hint2 = form.cleaned_data["hint2"]
            hint3 = form.cleaned_data["hint3"]
            hints= [hint1,hint2,hint3]
            obj.hints =hints
            obj.save()
        return HttpResponseRedirect('/admin/enterdata/enterdata')


def searchdata(request):
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()
        if len(querystring) == 0:
            return redirect('/search/')

        try:
            search_type = request.GET.get('type')

        except Exception:
            pass

        count = {}
        results= EnterData.objects.filter(Q(last_name__icontains=querystring) |\
                                                   Q(work_exp__icontains=querystring))

        return render(request, 'enterdata/results.html', {
            'querystring': querystring,
            'results': results,
        })
    else:
        return render(request, 'enterdata/search.html', {})
