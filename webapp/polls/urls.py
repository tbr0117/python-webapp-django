from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:QuestionId>/', views.detail, name="detail"),
    path("<int:QuestionId>/result", views.result, name="result"),
    path("<int:QuestionId>/vote", views.vote, name="vote"),
]