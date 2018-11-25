from django import forms
from .import models


class Add_image(forms.ModelForm):
    class Meta:
        model=models.Question
        fields=["question_text_image","option1_image","option2_image","option3_image","option4_image"]
