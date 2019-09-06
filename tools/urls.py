from django.urls import path
from . import views
from .controller import collectionView,faceRecognitionView


urlpatterns = [
    path('index',views.index),
    path('collection',collectionView.collection_html),
    path('face_recognition',faceRecognitionView.face_recognition_html),
]
