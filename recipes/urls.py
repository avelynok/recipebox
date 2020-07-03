from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add_author/', views.add_author, name='add_author'),
    path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('author/<int:id>/', views.author_detail, name='author_detail'),
    path('login/', views.loginview, name='loginview'),
    path('logout/', views.logoutview, name='logoutview')
]