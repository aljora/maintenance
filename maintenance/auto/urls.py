from . import views
from django.urls import path

app_name = "auto"
urlpatterns = [
    path('', views.CarListView.as_view(), name='index'),
    path(
        'cars/<int:pk>/',
        views.CarDetailView.as_view(),
        name='car-detail'
    ),
    path(
        'newinspection',
        views.InspectServiceCreateView.as_view(),
        name='newinspection'
    ),
]
