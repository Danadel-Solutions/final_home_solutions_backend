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

# from .views import (
#     get_properties,
#     get_property,
#     create_property,
#     update_property,
#     get_user_properties,
#     upload_image,
# )
from .views import (
    PropertyListView,
    PropertyDetailView,
    PropertyCreateView,
    PropertySearchView,
)

urlpatterns = [
    path("properties/", PropertyListView.as_view(), name="properties"),
    # path("user/properties/<str:pk>/", get_user_properties, name="get-user-properties"),
    path("properties/add/", PropertyCreateView.as_view(), name="property-create"),
    path("properties/search/", PropertySearchView.as_view(), name="property-search"),
    path("properties/<str:pk>/", PropertyDetailView.as_view(), name="property"),
    # path("properties/update/<str:pk>/", update_property, name="property-update"),
    # path("uploads/", upload_image),
]
