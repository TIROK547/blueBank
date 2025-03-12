from django.urls import path
from .views import my_account
urlpatterns = [
    path("account/<str:username>",my_account)
]