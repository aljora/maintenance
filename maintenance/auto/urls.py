from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'newinspection',
        views.InspectServiceCreateView.as_view(),
        name='newinspection'),
]
