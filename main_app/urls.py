from django.urls import path
from . import views

urlpatterns = [
   path('', views.Home.as_view(), name="home"),  
    path('about/', views.About.as_view(), name="about"),
    path('accounts/business/signup/', views.BusinessSignup.as_view(), name="business_signup"),
    path('business/<int:pk>/', views.BusinessDetail.as_view(), name="business_detail"),
    path('business_redirect/', views.BusinessRedirect.as_view(), name="business_redirect"),
    path('accounts/individual/signup/', views.IndividualSignup.as_view(), name="individual_signup"),
    path('user/profile/<int:pk>/', views.IndividualDetail.as_view(), name="individual_detail"),
    path('profile_redirect/', views.IndividualRedirect.as_view(), name="individual_redirect"),
    path('business/<int:pk>/listings/new/', views.JobPostCreate.as_view(), name="job_post_create"),
    path('listings/<int:pk>/', views.JobPostDetail.as_view(), name="job_post_detail"),
    path('listings/<int:pk>/update/', views.JobPostUpdate.as_view(), name="job_post_update"),
    path('listings/<int:pk>/delete/', views.JobPostDelete.as_view(), name="job_post_delete"),
    path('user/profile/<int:pk>/reviews/new/', views.ReviewCreate.as_view(), name="review_create"),
    path('reviews/<int:pk>/', views.ReviewDetail.as_view(), name="review_detail"),
    #path('users/<int:pk>/edit/', views.IndividualUpdate.as_view(), name="profile_update"),
 
]