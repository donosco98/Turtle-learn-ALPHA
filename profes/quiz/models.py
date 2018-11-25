from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
            return self.name
def upload_location(instance,filename):
    return "%s/%s" %(instance.id,filename)

class Question(models.Model):

    question_text=models.TextField(null=True,blank=True)
    question_text_image=models.ImageField(upload_to=upload_location, null=True,blank=True)
    #width_field=models.IntegerField(default=0)
    #height_field=models.IntegerField(default=0)
    option1_image=models.ImageField(null=True,blank=True)
    option2=models.TextField(null=True,blank=True)
    option2_image=models.ImageField(null=True,blank=True)

    option3=models.TextField(null=True,blank=True)
    option3_image=models.ImageField(null=True,blank=True)

    option4=models.TextField(null=True,blank=True)
    option4_image=models.ImageField(null=True,blank=True)
    response=models.CharField(max_length=90,default="option5",null=True,blank=True)
    answer=models.CharField(max_length=90,default="",null=True,blank=True)

    subject=models.CharField(max_length=90,default="",null=True,blank=True)
    chapter=models.CharField(max_length=90,default="",null=True,blank=True)
    subtopic=models.CharField(max_length=90,default="",null=True,blank=True)
    exam= models.ForeignKey(Test, on_delete=models.CASCADE,null=True,blank=True)
    difficulty=models.CharField(max_length=100,default="medium")
