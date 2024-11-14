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
    

class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()
    favorite_guidances = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "profile_image", "favorite_guidances"]

    def get_profile_image(self, instance):
        profile_image = instance.profile.profile_img
        if profile_image:
            # return the url of the profile image
            request = self.context.get("request")
            return request.build_absolute_uri(profile_image.url)
        # otherwise return None
        return None
    
    def get_favorite_guidances(self, instance):
        return list(instance.profile.favorite_guidances.values_list("id", flat=True))

    
    def validate_first_name(self, value):
        if not value:
            raise serializers.ValidationError("The user need to provide the first name")
        return value
    
    def validate_last_name(self, value):
        if not value:
            raise serializers.ValidationError("The user need to provide the last name")
        return value

class FavoriteGuidanceSerializer(serializers.ModelSerializer):
    religion = serializers.SerializerMethodField()

    class Meta:
        model = Guidance
        fields = ["id", "title", "content", "image", "religion"]

    def get_religion(self, obj):
        return obj.get_religion_display()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["profile_img"]
