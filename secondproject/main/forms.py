from django import forms 
from .models import task , category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class taskform(forms.ModelForm) :
    class Meta :
        model = task
        fields = ["title" , "description" , "status" , "priority" , "due_date" , "category"]

        widgets = {
            "title" : forms.TextInput(attrs={"class " : "form-control"}),
            "description" : forms.Textarea(attrs={"class" : "form-control"}),
            "status" : forms.Select(attrs={"class" : "form-control"}),
            "priority" : forms.NumberInput(attrs={"class" : "form-control"}),
            "due_date" : forms.DateInput(attrs={"class" : "form-control" , "type" : "date"}),
            "category" : forms.Select(attrs={"class" : "form-control"})
        }


class categoryform(forms.ModelForm) :
    class Meta : 
        model =category
        fields = ["name" , "description"]

        widgets = {
            "name" : forms.TextInput(attrs={"class" : "form-control"}),
            "description" : forms.Textarea(attrs={"class" : "form-control"})
        }


class loginform(AuthenticationForm) :
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class" : "form-control" ,
        "placeholder" : "username" , 
        "id": "floatingUsername",
        "style": "width: 500px; height: 40px; font-size: 16px;",
        "autofocus" : True }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class" : "form-control form-control-sm" , 
        "placeholder" : "password",
        "style": "width: 500px; height: 40px; font-size: 16px;",
        "id": "floatingPassword",
    }))


class signupform(forms.ModelForm) :
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'floatingPassword' }))
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'floatingPassword' }) , label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Username',
                'id': 'floatingUsername'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                'id': 'floatingEmail'
            })
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")