from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows/<int:show_id>', views.show_results),
    path('create_show', views.create_show),
    path('edit_show', views.show_update),
    path('delete/<int:show_id>', views.delete),
]