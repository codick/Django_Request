from django.urls import path
from task_django import views

urlpatterns = [
    path('', views.task),
    path('user/', views.user),
    path('error/', views.page_not_found_view),
    path('user/<login>', views.user),
    path('user/<login>/<folder_name>', views.user),
    path('user/<login>/<folder_name>/<post_number>', views.user)
]


