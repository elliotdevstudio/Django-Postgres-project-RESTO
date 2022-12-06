from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name="home"),
  path('about/', views.About.as_view(), name="about"),
  path('accounts/individual/signup/', views.IndividualProfileCreate.as_view(), name="individual_signup"),
  path('accounts/business/signup/', views.BusinessProfileCreate.as_view(), name="individual_signup"),
  path('profile/<int:pk>/', views.IndividualDetail.as_view(), name="individual_detail"),
  path('profile/<int:pk>/', views.BusinessDetail.as_view(), name="business_detail"),
 #path('profile_redirect/', views.ProfileRedirect.as_view(), name="profile_redirect"),
  
]