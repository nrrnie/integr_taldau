from django.urls import path
from . import views


urlpatterns = [
    path("insert-all-chapters/", views.InsertAllChapters.as_view()),
    path("insert-all-periods/", views.InsertAllPeriods.as_view()),
    path("insert-all-indices/", views.InsertAllIndices.as_view()),
    path("add-one-index-info/", views.AddOneIndexInfo.as_view()),
    path("add-all-index-info/", views.AddAllIndexInfo.as_view()),
    path("insert-index-data/", views.InsertIndexData.as_view()),
    path("insert-index-data-param/", views.InsertIndexDataParam.as_view()),
]