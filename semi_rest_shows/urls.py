from django.urls import path, include

urlpatterns = [
    path('', include('semi_rest_app.routes')),
]