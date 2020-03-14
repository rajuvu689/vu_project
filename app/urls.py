from django.urls import path
from . import views
urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.HomePageView.as_view(), name="home"),
    # path('detail/<int:id>/', views.detail, name="detail"),
    path('detail/<int:pk>/', views.ContactDetailView.as_view(), name="detail"),
]
