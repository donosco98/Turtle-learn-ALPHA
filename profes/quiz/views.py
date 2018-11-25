from django.shortcuts import render,redirect,get_object_or_404
from . forms import Add_image
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from . models import Question,Test
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
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







@csrf_exempt
def quiz(request,id):
    ques=Question.objects.get(pk=id)
    idea=id
    quest=Question.objects.all()

    option=request.POST.get('hash')
    print(option)
    num=ques.response
    num=num[6]
    print(num)

    return render(request,'quiz.html',{'ques':ques,'quest':quest,'idea':idea,'num':num})

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
