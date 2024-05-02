from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='employee-dashboard'),
    path('leave_request/', views.leave_request, name='leave-request'),
    path('post_leave_request/', views.post_leave_request, name='post-leave'),
    path('leave_report/', views.leave_report, name='leave-report'),
    path('login/', views.login, name='employee-login'),
    path('post_login/', views.post_login, name='post-login')
]