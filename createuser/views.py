from django.shortcuts import render
from rest_framework.response import Response

from .models import users
from .serializers import usersSerializers
from rest_framework.views import APIView



class ListusersAPIView(APIView):
    def get(self,request):
        myusers = users.objects.all()
        serializer = usersSerializers(myusers, many=True)
        return Response(serializer.data)


class CreateusersAPIView(APIView):
    def post(self, request):
        serializer = usersSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class UpdateusersAPIView(APIView):
    def post(self, request, pk):
        myuser = users.objects.get(id=pk)
        serializer = usersSerializers(instance=myuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class DeleteusersAPIView(APIView):
    def delete(self, request, pk):
        myuser = users.objects.get(id=pk)
        myuser.delete()
        return Response({'user id': 'Deleted'})
