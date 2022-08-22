from django.urls import path
from .views import RegisterVirew

urlpatterns = [
    path('register',RegisterVirew.as_view()),
]

