from django.shortcuts import render, get_object_or_404
from recipes.models import Author, RecipeItems

# Create your views here.
def index(request):
    data = RecipeItems.objects.all() 
    return render(request, 'index.html', {'data': data})

def author_detail(request, id):
    author = get_object_or_404(Author,id=id)
    recipe = RecipeItems.objects.filter(author=id)
    data = RecipeItems.objects.all()
    return render(request, 'author_detail.html', {'author': author, 'recipe': recipe, 'data': data})

def recipe_detail(request, id):
    recipe = get_object_or_404(RecipeItems,id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

