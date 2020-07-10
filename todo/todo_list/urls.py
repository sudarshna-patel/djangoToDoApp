from django.urls import path
from .views import home_view, delete, cross_off, uncross, edit

urlpatterns = [
    path('', home_view, name="home"),
    path('<id>/delete', delete, name='delete'),
    path('<id>/cross_off', cross_off, name='cross_off'),
    path('<id>/uncross', uncross, name="uncross"),
    path('<id>/edit', edit, name="edit"),
]