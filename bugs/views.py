from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import Bugs
from . import forms

# Create your views here.

def bugs(request):
    bugs = Bugs.objects.all().order_by('date')
    print("Views sees bugs has this in it: " + str(bugs))
    return render(request, 'bugs_list.html', {'bugs': bugs})

def bug_detail(request, slug):
    bugs = Bugs.objects.get(slug=slug)
    #bugs = Bugs.objects.get(slug=slug)
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

@login_required(login_url="/accounts/login/")
def mybugs_view(request):
    if request.method == 'GET':
        myusername = request.user.username
        mybugs = Bugs.objects.all()
        #for articles in myarticles:
            #articles.pk = None
            #articles.save()
        mybug_ids = []
        for bug in mybugs:
            temp_author_storage = bug.author
            bug_name = str(temp_author_storage)
            if bug_name == myusername:
                mybug_ids.append(bug)
        return render(request, 'mybugs.html', {'bugs': mybug_ids})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})