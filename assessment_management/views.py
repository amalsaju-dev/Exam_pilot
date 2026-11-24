from django.shortcuts import render

# Create your views here.

from assessment_management.models import Assessment

from assessment_management.serializer import AssessmentSerializer

from rest_framework import authentication,permissions

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class AssessmentListCreateView(ListCreateAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AssessmentSerializer

    def get_queryset(self):
        return Assessment.objects.filter(tutor=self.request.user)

    def perform_create(self, serializer):
        serializer.save(tutor = self.request.user)

class AssessmentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes =[authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = AssessmentSerializer

    def get_queryset(self):

        return Assessment.objects.filter(tutor = self.request.user)
        

    
