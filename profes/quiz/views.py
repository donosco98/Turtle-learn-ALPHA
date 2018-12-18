from django.shortcuts import render,redirect,get_object_or_404
from . forms import Add_image
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login
from . models import Question,Test
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from .forms import UserForm

def question_list(request):
    ques=Question.objects.all()

    return render(request,'questions.html',{'ques':ques},)

def question_details(request,id):
    ques=Question.objects.get(pk=id)
    return render(request,'question_detail.html',{'ques':ques})


def add_question(request):
    test=Test.objects.all()
    que=request.POST.get('Question')
    option1=request.POST.get('option1')
    option2=request.POST.get('option2')
    option3=request.POST.get('option3')
    option4=request.POST.get('option4')
    correct=request.POST.get('CorrectAns')
    sub=request.POST.get('subjects')
    chap=request.POST.get('chapters')
    subt=request.POST.get('subtopics')
    exam2=request.POST.get('exams')
    diff=request.POST.get('difficulty')
    img=request.POST.get('image')

    if diff in ["Medium","Easy","Hard"]:
        t=Test.objects.get(name=exam2)
        p=Question.objects.create(question_text=str(que),option1=str(option1),option2=str(option2),option3=str(option3),option4=str(option4),answer=str(correct),subject=str(sub),chapter=str(chap),subtopic=str(subt),exam=t,difficulty=str(diff))

        id=p.id
        p.save
        if img=="yes":
            return redirect('http://127.0.0.1:8000/list/image/'+str(id)+'/')
        print("yes")

    return render(request,'form.html',{'test':test})



def add_image(request,id):
    instance=get_object_or_404(Question,id=id)

    if request.method == 'POST':
        form = Add_image(request.FILES,instance=instance)


        if form.is_valid():
            instance=form.save()

            print("********")
            instance.save()
            print("$$$$$$$$$$")




    return render(request,'image_form.html',{'form':form} ,)





@login_required
@csrf_exempt
def quiz(request,id):
    ques=Question.objects.get(pk=id)
    idea=id
    quest_chem=Question.objects.filter(exam__name="jee main 1",subject="Chemistry")
    quest_phy=Question.objects.filter(exam__name="jee main 1",subject="Physics")
    quest_math=Question.objects.filter(exam__name="jee main 1",subject="Mathematics")


    test=Test.objects.get(name="jee main 1")
    print(test.time)
    option=request.POST.get('hash')
    print(option)
    num=ques.response
    num=num[6]
    print(num)

    return render(request,'quiz.html',{'ques':ques,'quest_chem':quest_chem,'quest_phy':quest_phy,'quest_math':quest_math,'idea':idea,'num':num,'test':test,})

def result(request):
    quest=Question.objects.filter(exam__name="jee main 1")
    right=0
    wrong=0
    attempted=0
    print(quest)
    for qs in quest :
        if qs.response==qs.answer:
            right=right+1
            qs.status="right"
            qs.save()
        elif qs.response=="option5":
            attempted=attempted+1

        else:
            wrong=wrong+1
            qs.status="wrong"
            qs.save()
        ques_wrong=Question.objects.filter(status="wrong")
        ques_right=Question.objects.filter(status="right")
    return render(request,'result.html',{'right':right,'wrong':wrong,'attempted':attempted,'ques_right':ques_right,'ques_wrong':ques_wrong})




@csrf_exempt
def data(request):

    if request.method == 'POST':
        if 'pieFact' in request.POST:
            pieFact = request.POST['pieFact']
            id2=request.POST['ide']
            idea=request.POST['idea']
            Question.objects.filter(pk=idea).update(response=pieFact)
            print(pieFact,id2,idea)
            #return redirect('http://127.0.0.1:8000/list/')
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')

@csrf_exempt
def data2(request):

    if request.method == 'POST':
        if 'totalSeconds' in request.POST:
            Fact = request.POST['totalSeconds']
            Test.objects.filter(name="jee main 1").update(time=int(Fact))            #Question.objects.filter(pk=idea).update(response=pieFact)
            qtime=request.POST['questionTime']
            id2=request.POST['id2']
            Question.objects.filter(pk=id2).update(time_taken=int(qtime))

            #return redirect('http://127.0.0.1:8000/list/')
            return HttpResponse('success') # if everything is OK
    # nothing went well
    return HttpRepsonse('FAIL!!!!!')



def quiz_list(request):
    test=Test.objects.filter(name="jee main 1")
    qs=Question.objects.all()
    q1=Question.objects.all()[:1].get()
    id=q1.id
    print(qs)
    for t in test :
        t.time=3600
        t.save()

    for q in qs:
        q.response="option5"
        q.time_taken=0
        q.save()

    return render(request,"landing.html",{'test':test,'ide':id})



class UserFormView(View):
    form_class=UserForm
    template_name='register.html'
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user=authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("http://127.0.0.1:8000/l")

        return render(request,self.template_name,{'form':form})
