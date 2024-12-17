from django.urls import path
from . import views

urlpatterns = [
    path('generate-question/', views.GenerateQuestionView.as_view(), name='generate_question'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('create-quiz/', views.CreateQuizView.as_view(), name='create_quiz'),
    path('submit-quiz/', views.SubmitQuizView.as_view(), name='submit_quiz'),
    path('generate_hint/', views.GenerateHintView.as_view(), name='generate_hint'),
]
