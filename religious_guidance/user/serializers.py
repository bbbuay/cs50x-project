from rest_framework import serializers
from django.contrib.auth.models import User
from guidance.models import Guidance
from .models import UserProfile

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password_confirmation = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password", "password_confirmation"]

    def validate(self, attrs):
        # check if the given password and confirmation password are the same or not
        if attrs["password"] != attrs["password_confirmation"]:
            raise serializers.ValidationError("The passwords do not match. Please try again.")
        
        # user's email should not exist in the database for another user
        if attrs["email"] in User.objects.values_list("email", flat=True):
            raise serializers.ValidationError("This email address is already registered.")
        
        return super().validate(attrs)
    
    def create(self, validated_data):
        # create user with the given question
        user = User.objects.create(
            username = validated_data["username"],
            email = validated_data["email"],
            first_name = validated_data["first_name"],
            last_name = validated_data["last_name"],
        )

        # set the user password
        user.set_password(raw_password=validated_data["password"])
        user.save()

        return user
    

class UserProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "profile_image"]

    def get_profile_image(self, obj):
        profile_image = obj.profile.profile_img
        return profile_image if profile_image else None
