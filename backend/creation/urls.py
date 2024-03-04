from django.urls import path
from . import views



urlpatterns = [
    path('user-register/', views.UserRegisterApi),
    path('user-register/<int:pk>/',views.OperationByOne),
    path('loan/', views.LoanApi.as_view()),
    path('hello/', views.hello_world, name='hello-world'),
]

