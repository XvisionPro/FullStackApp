from rest_framework import serializers
from .models import User, Post

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'isAdmin', 'welcomeCode']
        
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        
class PostDetailSerializer(serializers.ModelSerializer):
    
    user = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = '__all__'
        
    def get_user(self, obj):
        return f'User ID: {obj.user.id}, E-Mail: {obj.user.email}'