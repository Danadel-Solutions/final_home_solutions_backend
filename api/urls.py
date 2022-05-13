# from django.urls import path
# from .views import PropertyListView, PropertyDetailView
# urlpatterns = [
#     path('properties/', PropertyListView.as_view()),
#     path('properties/<int:pk>/', PropertyDetailView.as_view())
# ]
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import PropertyViewSet
router = SimpleRouter()
router.register('properties', PropertyViewSet, basename='properties')
urlpatterns = router.urls