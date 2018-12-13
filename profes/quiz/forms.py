from django import forms
from .import models
from django.contrib.auth.models import User



class Add_image(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=["question_text_image","option1_image","option2_image","option3_image","option4_image"]

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']
        
