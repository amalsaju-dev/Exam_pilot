from django.shortcuts import render

# Create your views here.

from rest_framework.generics import CreateAPIView,RetrieveUpdateAPIView

from accounts.models import TrainerProfile

from accounts.serializer import UserSerializer,TrainerProfileSerializer,StudentProfileSerializer

from rest_framework import authentication,permissions


class UserSignUpView(CreateAPIView):

    serializer_class = UserSerializer


class TrainerProfileView(RetrieveUpdateAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = TrainerProfileSerializer

    def get_object(self):
         
         return TrainerProfile.objects.get(user = self.request.user)






