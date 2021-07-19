from django.urls import path, include

from .views import LocationDetails, LocationViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("locations", LocationViewSet, basename="locations")
router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path('locations/<int:my_id>/', LocationDetails.as_view()),
    path('', include(router.urls))

]
