from django.shortcuts import render
from django.http import HttpResponse


def list_html(request):
    context = {}
    return render(request, 'notebook/list.html', context)


def edit_html(request):
    context={}
    return render(request, 'notebook/edit.html', context)


def notebook_save(request):
    print(request.POST['text'])
    print(request.POST['html'])
    return HttpResponse("success")

