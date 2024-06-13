from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImages
        fields = ['id', 'image', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    images = serializers.ListField(child=serializers.ImageField(), write_only=True)
    host_id = serializers.IntegerField(source='host.id', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'host', 'host_name','host_id', 'host_initials', 'property_title', 'slug', 'property_type', 'property_price', 'bedroom_no', 'bathroom_no', 'property_location', 'property_description', 'created_at', 'images', 'contact_info']
        extra_kwargs = {
            'host': {'write_only': True},
        }
        
    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        post = Post.objects.create(**validated_data)
        for image_data in images_data:
            PostImages.objects.create(post=post, image=image_data)
            
        return post
    
class RetrievePostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(child=serializers.ImageField(), write_only=True, required=False)  
    host_id = serializers.IntegerField(source='host.id', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'host', 'host_name', 'host_id', 'host_initials', 'slug', 'property_title', 'property_type', 'property_price', 'bedroom_no', 'bathroom_no', 'property_location', 'property_description', 'created_at', 'images', 'uploaded_images', 'contact_info']
        extra_kwargs = {
            'host': {'write_only': True},
        }
    
    