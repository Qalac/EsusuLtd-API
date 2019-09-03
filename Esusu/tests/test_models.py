from django.test import TestCase
from ..models import *

class TestUserModel(TestCase):
    def setUp(self):
        User.objects.create()

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
#This tests that a profile is created alongside a user profile
    def test_info_creation(self):
        self.assertEqual(User_Info.objects.count(), 1)

class TestGroupModel(TestCase):
    def setUp(self):
        Group.objects.create()

    def test_group_creation(self):
        self.assertEqual(Group.objects.count(), 1)

