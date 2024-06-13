from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import *

# View for the root page
class UserHomeView(APIView):
    permission_classes= [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        data = serializer.data
        data['is_staff'] = user.is_staff
        return Response(data, status=status.HTTP_200_OK)

# View to handle user details
class userDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset= User.objects.all()
    persmission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
# View that handles user registeration
class ListCreateUserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

# View that handles post creation
class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        data = request.data.copy()
        data['host'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save(host=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
class ListAllPosts(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetrievePostSerializer
    queryset = Post.objects.all().order_by('-created_at')
    
# View that handles post retrieval, update and deletion
class RetrieveDestroyPostView(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = RetrievePostSerializer
    queryset = Post.objects.all()
