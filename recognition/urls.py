from django.urls import path

from recognition.views import recognitionHome

urlpatterns = [
    path('', recognitionHome),
]