from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from django.contrib import messages
from django import forms
from .models import *
from django.contrib.auth.models import User , auth
from .filters import IssueFilter1,IssueFilter


# Create your views here.

def index(request):
  #  case = Issue.objects.all()
    return render(request, 'index.html')


def RimErrors(request):
    case = Issue.objects.all()
    return render(request, 'RimErrors.html',{'case':case})



def upload(request):
    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES,)
        if form.is_valid():
            Issue=form.save(commit=False)
            Issue.user =request.user
            form.save()
            messages.info(request, 'YOUR DATA HAS BEEN UPLOADED')

    else:
        form = PostForm()
    return render(request, 'upload.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')


def search(request):
    #Issue_list = Issue.objects.all(user=request.user)
    Issue_list = Issue.objects.all()
    Issue_filter = IssueFilter(request.GET, queryset=Issue_list)
    return render(request, 'user_list.html', {'filter': Issue_filter})


def search1(request):
    #case = Issue.objects.all()
    return render(request, 'user_list1.html')


'''def approved(request):
    case = Issue.objects.get(user_id=auth.user_logged_in)
    return render(request, 'approved.html', {'case': case})
'''
def approved(request):
    if request.user.is_authenticated:
        user = request.user
        case = Issue.objects.filter(user=user,show=True)
        return render(request ,'approved.html', {'case': case})
    else:
        messages.info(request, 'PLEASE LOGIN TO SEE YOUR APPROVED UPLOADS ')
        return render(request, 'approved.html',{})


def unapproved(request):
    if request.user.is_authenticated:
        user = request.user
        case = Issue.objects.filter(user=user, show=False)
        return render(request, 'unapproved.html',{'case':case})
    else:
        messages.info(request, 'PLEASE LOGIN TO SEE YOUR UN-APPROVED UPLOADS ')
        return render(request, 'unapproved.html',{})

