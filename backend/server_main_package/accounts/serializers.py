from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    password = serializers.CharField(min_length=8, max_length=32, write_only=True)
    email = serializers.EmailField(max_length=50, allow_blank=False)
    age = serializers.IntegerField(min_value=18)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "age"]

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data["email"]
        password = validated_data["password"]
        age = validated_data['age']
        user_obj = User(username=username, email=email, age=age)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
