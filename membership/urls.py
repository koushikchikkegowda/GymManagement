from django.urls import path,include
from . import views

urlpatterns = [
    path('membershipList/',views.membershipList,name="membershipList"),
    path('membershipDelete/<int:pk>',views.membershipDelete,name="membershipDelete"),
    path('addMembership/',views.addMembership,name="addMembership"),
    path('addMembership_item/',views.addMembership_item,name="addMembership_item"),
    path('membership_edit/<int:pk>' ,views.membership_edit, name="membership_edit"),
    path('membershipEdit_item/<int:pk>' ,views.membershipEdit_item, name="membershipEdit_item"),
]