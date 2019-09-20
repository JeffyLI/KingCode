from django.shortcuts import render


def notebook_html(request):
    context = {}
    return render(request,'notebook.html', context)
