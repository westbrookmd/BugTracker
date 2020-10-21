from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from articles.models import Article
from django.contrib.auth.decorators import login_required

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

@login_required(login_url="/accounts/login/")
def myarticles_view(request):
    if request.method == 'GET':
        myusername = request.user.username
        myarticles = Article.objects.all()
        print("Here are all of the articles:" + str(myarticles))
        #for articles in myarticles:
            #articles.pk = None
            #articles.save()
        myarticle_ids = []
        for articles in myarticles:
            temp_author_storage = articles.author
            print("For this article:" + str(articles))
            article_name = str(temp_author_storage)
            print("Article author:" + article_name)
            if article_name == myusername:
                print("Article_name is equal to myusername!")
                myarticle_ids.append(articles)
                print("Current list of articles that match my username:" + str(myarticle_ids))
        return render(request, 'accounts/myarticles.html', {'articles': myarticle_ids})
    else:
        form = UserCreationForm()
        return render(request, 'accounts/signup.html', {'form':form})
