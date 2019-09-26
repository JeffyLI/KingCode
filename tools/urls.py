from django.urls import path
from . import views
from .controller import collectionView,faceRecognitionView,notebookView


urlpatterns = [
    path('index',views.index),
    path('collection',collectionView.collection_html),
    path('notebook',notebookView.list_html),
    path('notebook/edit',notebookView.edit_html),
    path('notebook/save',notebookView.notebook_save),
    path('face_recognition',faceRecognitionView.face_recognition_html),
]
