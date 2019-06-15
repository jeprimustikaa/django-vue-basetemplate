from django.urls import path
from .views import ListQuestionsView

urlpatterns = [
    path('questions/', ListQuestionsView.as_view(), name="questions")
]
