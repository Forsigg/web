from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new(request, *args, **kwargs):
    questions = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'new.html', context={
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })

def popular(request):
    questions = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, 10)
    paginator.baseurl = '/popular?page='
    page = paginator.page(page)
    return render(request, 'popular.html', context={
        'questions': page.object_list,
        'paginator': paginator,
        'page': page
    })


def question(request, id):
    question = get_object_or_404(Question, id=id)
    answers = question.answer_set.all()

    return render(request, 'question.html', context={
        'question': question,
        'answers': answers,
    })


