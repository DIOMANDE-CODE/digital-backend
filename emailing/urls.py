from django.urls import path
from .views import EmailingList

urlpatterns = [
    path('email/', EmailingList.as_view()),
]