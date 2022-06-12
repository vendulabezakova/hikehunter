from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path("hike_list", views.HikeListView.as_view(), name="hike_list"),
    path('hike/<int:pk>', views.HikeDetailView.as_view(), name='hike_detail'),
    path('create_hike', views.HikeCreateView.as_view(), name="create_hike"),
    path('register', views.RegisterView.as_view(), name='register'),
]