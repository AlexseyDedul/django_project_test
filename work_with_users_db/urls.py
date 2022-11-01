from django.contrib import admin
from django.urls import path, include

from work_with_users_db.views import UsersView, CastomerView

urlpatterns = [
    path('users/', UsersView.as_view()),
    path('users/<int:pk>', UsersView.as_view()),
    path('castomer/', CastomerView.as_view()),
]

