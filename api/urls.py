# from django.urls import path
# from .views import PropertyListView, PropertyDetailView
# urlpatterns = [
#     path('properties/', PropertyListView.as_view()),
#     path('properties/<int:pk>/', PropertyDetailView.as_view())
# ]
# from django.urls import path
# from rest_framework.routers import SimpleRouter
# from .views import PropertyViewSet
# router = SimpleRouter()
# router.register('properties', PropertyViewSet, basename='properties')
# urlpatterns = router.urls

from django.urls import path
from .views import (
    get_properties,
    get_property,
    create_property,
    update_property,
    get_user_properties,
)

urlpatterns = [
    path("properties/", get_properties, name="properties"),
    path("user/properties/<str:pk>/", get_user_properties, name="get-user-properties"),
    path("properties/add/", create_property, name="property-create"),
    path("properties/<str:pk>/", get_property, name="property"),
    path("properties/update/<str:pk>/", update_property, name="property-update"),
]
