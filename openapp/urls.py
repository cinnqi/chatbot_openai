from django.urls import path 
from openapp import views
from django.views.generic.base import RedirectView

urlpatterns=[
    path("", RedirectView.as_view(url='/login/', permanent=False)),
    path("main/", views.HomeView.as_view(), name='main'),
    path("sign-up/", views.SignUp.as_view(), name='signup'),
    path("delete/", views.DeleteHistory, name='deleteChat'),
    path("login/", views.LoginView.as_view(), name="login"),
]