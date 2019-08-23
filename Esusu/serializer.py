from .models import *
from rest_framework import serializers


# serializer_class for carrying out CREATE action for user registration
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


# serializer_class for carrying out CREATE action for group setup
class GroupCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', 'group_description', 'max_capacity', 'searchable'] 


# serializer_class for carrying out RETRIEVE action for searchable groups
class GroupFindSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['group_name', 'group_description', 'searchable', 'max_capacity']


# serializer_class for carrying out RETRIEVE action for viewing amount_saved by members
class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['user', 'amount_saved']


# serializer_class for carrying out RETRIEVE action for viewing user ID and username
class ViewProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['id', 'user', 'group']


# serializer_class for carrying out UPDATE action for users.
class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Info
        fields = ['group', 'invite']

