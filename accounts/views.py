from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User

# Create your views here.

class UserView(APIView):
    def get(self,request):
        user_id=request.user.id
        UserObject=User.objects.get(id=user_id)
        serializer=UserSerializer(UserObject)
        return Response(serializer.data)
    
        

