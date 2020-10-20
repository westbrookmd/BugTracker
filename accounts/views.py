from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from articles.models import Article

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

#Authentication stuff begins
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')

def myarticles_view(request):
    if request.method == 'GET':
        myusername = request.user.username
        myarticles = Article.objects.all()
        #for articles in myarticles:
            #articles.pk = None
            #articles.save()
        for articles in myarticles:
            temp_author_storage = articles.author
            article_name = str(temp_author_storage)
            myarticle_ids = []
            if article_name == myusername:
                myarticle_ids.append(articles)
        return render(request, 'accounts/myarticles.html', {'articles': myarticle_ids})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})
