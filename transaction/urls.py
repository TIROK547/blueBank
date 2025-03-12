from django.urls import path
from .views import my_account,get_loan
urlpatterns = [
    path("account/<str:username>",my_account),
    path("loan/<int:darkhast>",get_loan)
]