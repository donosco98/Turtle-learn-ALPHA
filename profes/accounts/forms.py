from django import forms

from django.contrib.auth import (
    authenticate,get_user_model,login,logout,


)


User=get_user_model()



class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get("password")
        user=authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("this user sucks")

        if not user.check_password(password):
            raise forms.ValidationError("Incorrect password")

        if not user.is_active:
            raise forms.ValidationError("this user is not longer ")


        return super(UserLoginForm,self).clean(*args,**kwargs)



class UserRegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=[

        'username','email','password'
        ]
