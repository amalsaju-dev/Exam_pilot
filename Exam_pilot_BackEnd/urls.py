"""
URL configuration for Exam_pilot_BackEnd project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from rest_framework.authtoken.views import ObtainAuthToken

from accounts.views import UserSignUpView

from accounts.views import TrainerProfileView

from assessment_management.views import AssessmentListCreateView
from assessment_management.views import AssessmentRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),

    #user Sign up View
    path('sign/up/',UserSignUpView.as_view()),

    #retrieve
    path("trainer/profile/", TrainerProfileView.as_view()),

    #token
    path("token/",ObtainAuthToken.as_view()),

    #ASSESSMENT

    path("assessments/",AssessmentListCreateView.as_view()),

    path("assessments/<int:pk>/",AssessmentRetrieveUpdateDeleteView.as_view()),
]
