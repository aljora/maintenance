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
        'fuel/<int:pk>/',
        views.FuelDetailView.as_view(),
        name='fuel-detail'
    ),
    path(
        'inspectservice/add',
        views.InspectServiceCreateView.as_view(),
        name='inspectserviceadd'
    ),
    path(
        'replaceservice/add',
        views.ReplaceServiceCreateView.as_view(),
        name='replaceserviceadd'
    ),
    path(
        'fuelservice/add',
        views.FuelServiceCreateView.as_view(),
        name='fuelserviceadd'
    ),
    path(
        'configurepart',
        views.PartCreateView.as_view(),
        name='configurepart'
    ),
    path(
        'configureinspection',
        views.InspectionCreateView.as_view(),
        name='configureinspection'
    ),
    path(
        'configurereplacement',
        views.ReplacementCreateView.as_view(),
        name='configurereplacement'
    )
]
