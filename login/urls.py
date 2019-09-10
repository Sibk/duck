from django.urls import path, re_path
import login.views as views

urlpatterns = [
    re_path(r'auth/', views.login_auth, name = 'default page'),
]

