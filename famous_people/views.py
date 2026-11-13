from rest_framework import generics, status
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from .serializers import FamousPeopleSerializer
from .models import FamousPeopleModel

class FamousApiView(APIView):
    def get(self, request):
        queryset_2 = FamousPeopleModel.objects.all()
        serializer_class = FamousPeopleSerializer(queryset_2, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        serializer = FamousPeopleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        post_new =FamousPeopleModel.objects.create(
            id = request.data['id'],
            title= request.data['title'],
            text= request.data['text'],

        )
        return Response(model_to_dict(post_new), status=status.HTTP_201_CREATED)

class FamousPeopleDetailAPIView(APIView):

    def get(self, request, pk):
        query = get_object_or_404(FamousPeopleModel, pk=pk)
        serializer = FamousPeopleSerializer(query)
        return Response(serializer.data)