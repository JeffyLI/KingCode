from django.urls import path
from . import views
from .controller import collectionView


urlpatterns = [
    path('index',views.index),
    path('collection',collectionView.collection)
]
