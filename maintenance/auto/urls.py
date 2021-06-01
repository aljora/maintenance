from . import views
from django.urls import path

app_name = "auto"
urlpatterns = [
    path('', views.CarListView.as_view(), name='index'),
    path(
        'car/<int:pk>/',
        views.CarDetailView.as_view(),
        name='car-detail'
    ),
    path(
        'part/<int:pk>/',
        views.PartDetailView.as_view(),
        name='part-detail'
    ),
    path(
        'inspection/<int:pk>/',
        views.InspectionDetailView.as_view(),
        name='inspection-detail'
    ),
    path(
        'replacement/<int:pk>/',
        views.ReplacementDetailView.as_view(),
        name='replacement-detail'
    ),
    path(
        'reportinspection/',
        views.InspectServiceCreateView.as_view(),
        name='reportinspectionpost'
    ),
    path(
        'reportinspection/<int:car>/',
        views.InspectServiceCreateView.as_view(),
        name='reportinspectionget'
    ),
    path(
        'configureinspection',
        views.InspectionCreateView.as_view(),
        name='configureinspection'
    )
]
