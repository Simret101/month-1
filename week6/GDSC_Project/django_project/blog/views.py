from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter

class CustomPagination(PageNumberPagination):
    page_size = 5 
    page_size_query_param = 'page_size'
    max_page_size = 100

@api_view(['POST',"GET"])
def getAll(request,format=None):
    if request.method=="GET":
        posts = Post.objects.all()
        
        filter_backends = [SearchFilter, OrderingFilter]
        search_fields = ['^title', '^content']

  
        paginator = CustomPagination()
        paginated_loans = paginator.paginate_queryset(posts, request)

        serializer = PostSerializer(paginated_loans, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method=="POST":
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])  
def post_detail(request,id,format=None):
    try:
        post=Post.objects.get(pk=id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer=PostSerializer(post)
        return Response(serializer.data)
    elif request.method=="PUT":
        serializer =PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.http_400)
    elif request.method=='DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
        