from django import forms
from recipes.models import Author

# Create your models here.
class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields =[
            'name',
            'bio',
        ]
        
class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=50)
    author = forms.ModelChoiceField(queryset= Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time = forms.CharField(max_length=15)
    instruction = forms.CharField(widget=forms.Textarea)
    
class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    