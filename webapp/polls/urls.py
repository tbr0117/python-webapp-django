from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:QuestionId>/', views.detail, name="detail"),
    path("<int:QuestionId>/results", views.results, name="results"),
    path("<int:QuestionId>/vote/", views.vote, name="vote"),
]