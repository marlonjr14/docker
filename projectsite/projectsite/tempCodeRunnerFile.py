from django.contrib import admin
from django.urls import path, include
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView 
from studentorg import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'), 

    path('orgmembers/', views.OrgMemberList.as_view(), name='orgmember-list'),
    path('orgmembers/add/', views.OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmembers/<int:pk>/', views.OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmembers/<int:pk>/delete/', views.OrgMemberDeleteView.as_view(), name='orgmember-delete'),

    path('students/', views.StudentList.as_view(), name='student-list'),
    path('students/add/', views.StudentCreateView.as_view(), name='student-add'),
    path('students/<int:pk>/', views.StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student-delete'),

    path('colleges/', views.CollegeList.as_view(), name='college-list'),
    path('colleges/add/', views.CollegeCreateView.as_view(), name='college-add'),
    path('colleges/<int:pk>/', views.CollegeUpdateView.as_view(), name='college-update'),
    path('colleges/<int:pk>/delete/', views.CollegeDeleteView.as_view(), name='college-delete'),

    path('programs/', views.ProgramList.as_view(), name='program-list'),
    path('programs/add/', views.ProgramCreateView.as_view(), name='program-add'),
    path('programs/<int:pk>/', views.ProgramUpdateView.as_view(), name='program-update'),
    path('programs/<int:pk>/delete/', views.ProgramDeleteView.as_view(), name='program-delete'),
]