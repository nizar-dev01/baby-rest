from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('create', views.CreateBlogView.as_view(), name="create")
]
