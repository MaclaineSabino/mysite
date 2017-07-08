from django.shortcuts import render,redirect
#from django.http import HttpResponse
from pools.models import Question,Choice

# Create your views here.

def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request,'index.html',{
        'questoes':questions
    })

def exibir(request,pk):
    #questao = Question()
    #if question_id=='1':
    #    questao=Question('Quem descobriu o Brasil?','2017-05-09')


    #if question_id=='2':
    #    questao=Question('Quem descobriu a América?','2017-06-01')


    #if question_id=='3':
    #    questao=Question('O que é uma bissetriz?','2017-06-03')



    questao=Question.objects.get(id=pk)
    choic = Choice.objects.filter(question=questao)
    choic_nulls = Choice.objects.filter(question=None)
    return render(request,'question.html',{'questao':questao,
                                           'choice':choic,
                                           'choice_nulls':choic_nulls})
def incluir(request,pk,pkc):
    questao = Question.objects.get(id=pk)
    choice = Choice.objects.get(id=pkc)
    choice.question=questao
    choice.save()
    choic = Choice.objects.filter(question=questao)
    choic_nulls = Choice.objects.filter(question=None)

    return render(request,'question.html',{'questao':questao,
                                           'choice':choic,
                                           'choice_nulls':choic_nulls})

def results(request,pk):
    soma=0
   
    questao=Question.objects.get(id=pk)

    choic = Choice.objects.filter(question=questao)
    for val in choic:
        soma=soma+val.votes



    return render(request,'results.html',{'questao':questao,
                                           'choice':choic,
                                          'soma':soma}
                                          )

def vote(request,pk):

    choice = Choice.objects.get(id=pk)
    choice.votes=choice.votes+1
    choice.save()
    questao = choice.question

    return exibir(request,questao.pk)

def manage(request,pk):
    questao=Question.objects.get(id=pk)
    choic = Choice.objects.filter(question=questao)
    return render(request,'manage.html',{'questao':questao,
                                           'choice':choic})

def status(request,pk):
    questao=Question.objects.get(id=pk)
    questao.closed=not questao.closed
    questao.save()
    return exibir(request,questao.pk)

def remover(request,pk):
    choice = Choice.objects.get(id=pk)
    questao = choice.question
    choice.question=None
    choice.votes=0
    choice.save()
    return exibir(request,questao.pk)


