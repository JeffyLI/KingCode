from django.shortcuts import render


def face_recognition_html(request):
    context = {}
    return render(request, 'face_recognition.html', context)