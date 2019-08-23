from rest_framework import generics
from .serializer import *
from .models import *


class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def get_queryset(self):
        return User.objects.all()


class RegisterGroupView(generics.CreateAPIView):
    serializer_class = GroupCreateSerializer

    def get_queryset(self):
        return Group.objects.all()


class SearchableGroupView(generics.ListAPIView):
    serializer_class = GroupFindSerializer

    def get_queryset(self):
        return Group.objects.filter(searchable=True)


class MemberViewSet(generics.ListAPIView):
    serializer_class = MemberListSerializer
  
    def get_queryset(self):
        query = self.kwargs['group']
        return User_Info.objects.filter(group=query)


class AddUserToGroupView(generics.UpdateAPIView):
    serializer_class = UpdateSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return User_Info.objects.filter(id=pk)


class SeeViewSet(generics.ListAPIView):
    serializer_class = ViewProfileSerializer
    queryset = User_Info.objects.all()


