from django.conf.urls import include, url 
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'api', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url ENDPOINT for user registration
    url(r'register-user', views.RegisterUserView.as_view()),
    # url ENDPOINT registration of a group
    url(r'register-group', views.RegisterGroupView.as_view()),
    # url ENDPOINT for viewing searchable groups
    url(r'search-for-group', views.SearchableGroupView.as_view()),
    # url ENDPOINT for viewing groups members and their saved amount
    url(r'view-members/(?P<group>.+)/', views.MemberViewSet.as_view()),
    # url ENDPOINT for viewing user ID and their co_operative
    url(r'see-profile-list', views.SeeViewSet.as_view()),
    # url ENDPOINT for adding a user to a group via unique ID
    url(r'add-member/(?P<pk>.+)/', views.AddUserToGroupView.as_view()),
  ]

