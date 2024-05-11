from django.urls import path
from . import views

urlpatterns = [
    path("kitabpost/", views.KitabPostListCreate.as_view(), name="kitabpost-view-create")
]