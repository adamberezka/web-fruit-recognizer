from django.urls import path

from recognition.views import recognitionHome, recognitionDetail

urlpatterns = [
    path('', recognitionHome),
    path('<int:id>', recognitionDetail),
]