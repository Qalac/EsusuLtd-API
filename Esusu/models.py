from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.contrib.postgres.fields import *


# A user can only be an admin to exactly one group.
# Upon deletion of the admin account the group still remains
class Group(models.Model):
    group_admin = models.OneToOneField(User,null=True, on_delete=models.SET_NULL)
    group_name = models.CharField(max_length=500, null=True)
    group_description = models.TextField(max_length=500, null=True)
    max_capacity = models.IntegerField(default=0)
    # members is a derived field by getting users with the corresponding field value but will
    # be left blank for now
    members = models.CharField(max_length=100, null=True)
    # beneficiary_list is also a derived field from a query but will be left blank for now.
    beneficiary_list = models.CharField(max_length=100, null=True)
    Amount_to_be_saved = models.FloatField(default=0.0)
    searchable = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.group_name) 


# user info model serving as a user profile for data that isn't required during verification
class User_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, to_field='username', related_name='user')
    group = models.CharField(max_length=100, null=True)
    amount_saved = models.FloatField(default=0.0)
    invite = models.BooleanField(default=False)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

# creates a user profile upon a user creation.
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            usr_info = User_Info.objects.create(user=instance)
            usr_info.save()
    post_save.connect(create_user_profile, sender=User)

#configure group name to a certain format and strict regex
#write tests!!!
