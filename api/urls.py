from django.urls import path
from . import views

urlpatterns = [
    path('kitabpost/', views.KitabPostListCreate.as_view(), name="kitab-view-create"),
    path('kitabpost/<int:pk>/', views.KitabPostRetrieveUpdateDestory.as_view(), name=""),
    path('babPost/', views.BabPostListCreate.as_view()),
    path('babpost/<int:pk>/', views.BabPostRetrieveUpdateDestory.as_view(), name=""),
    path('fasalPost/', views.FasalPostListCreate.as_view()),
    path('fasalpost/<int:pk>/', views.FasalPostRetrieveUpdateDestory.as_view(), name=""),
]
