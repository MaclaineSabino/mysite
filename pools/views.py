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
    return render(request,'question.html',{'questao':questao,
                                           'choice':choic})
def results(request,pk):
    soma=0
    cont=0
    tabela={}
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
    choic = Choice.objects.filter(question=questao)

    return render(request,'results.html',{'questao':questao,
                                           'choice':choic})

def manage(request,pk):
    questao=Question.objects.get(id=pk)
    choic = Choice.objects.filter(question=questao)
    return render(request,'manage.html',{'questao':questao,
                                           'choice':choic})

def status(request,pk):
    questao=Question.objects.get(id=pk)
    choic = Choice.objects.filter(question=questao)
    questao.closed=not questao.closed
    questao.save()
    return render(request,'manage.html',{'questao':questao,
                                           'choice':choic})
def remover(request,pk):
    choice = Choice.objects.get(id=pk)
    questao = choice.question
    choice.delete()
    choic = Choice.objects.filter(question=questao)
    return render(request,'manage.html',{'questao':questao,
                                           'choice':choic})
