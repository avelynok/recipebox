from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from recipes.models import Author, RecipeItems
from recipes.forms import AddRecipeForm, AddAuthorForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    data = RecipeItems.objects.all()
    return render(request, 'index.html', {'data': data})

def recipe_detail(request, id):
    recipe = get_object_or_404(RecipeItems,id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = AddRecipeForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                RecipeItems.objects.create(
                    title = data['title'],
                    author = data['author'],
                    description = data['description'],
                    time = data['time'],
                    instruction = data['instruction'],
                )
            return HttpResponseRedirect(reverse('homepage'))
        form = AddRecipeForm()
            
    if not request.user.is_staff:
        form = AddRecipeForm(request.POST)
        if request.method == "POST" and form.is_valid():
            data = form.cleaned_data
            non_staff_author = RecipeItems.objects.create(
                title=data['title'],
                author=request.user.author,
                description=data['description'],
                time=data['time'],
                instructions=data['instructions'],
            )
            return HttpResponseRedirect(reverse('homepage'))
        form = AddRecipeForm()
    return render(request, 'AddRecipeForm.html', {'form': form})

def author_detail(request, id):
    author = get_object_or_404(Author,id=id)
    recipe = RecipeItems.objects.filter(author=id)
    data = RecipeItems.objects.all()
    return render(request, 'author_detail.html', {'author': author, 'recipe': recipe, 'data': data})

@login_required
def add_author(request):
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data['name'], 
            )
            newAuthor = Author.objects.create(
                name=data['name'],
                bio=data['bio'],
                user=new_user
            )
            newAuthor.save()
            return HttpResponseRedirect(reverse('homepage'))    
    if request.user.is_staff:
        return render(request, 'AddAuthorForm.html', {'form': form})
    return render(request, "notstaff.html")

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password']
                )
            if user:
                login(request, user)
                if "next" in request.POST:
                    return HttpResponseRedirect(
                    request.POST.get('next'))
                else:
                    return HttpResponseRedirect(reverse('homepage'))          
    form = LoginForm()
    return render(request, 'LoginForm.html', {'form': form})

def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage')) 