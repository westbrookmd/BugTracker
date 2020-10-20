from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Bugs
from . import forms
# Create your views here.

def bugs(request):
    bugs = Bugs.objects.all().order_by('date')
    print("Views sees bugs has this in it: " + str(bugs))
    return render(request, 'bugs_list.html', {'bugs': bugs})

def bug_detail(request, slug):
    bugs = Bugs.objects.get(slug=slug)
    return render(request, 'bug_detail.html', {'bug': bugs })

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreateBug(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('bugs:bugs')
    else:
        form = forms.CreateBug()
    return render(request, 'bugs_create.html', {'form':form})