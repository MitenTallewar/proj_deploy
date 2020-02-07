from rest_framework.routers import SimpleRouter
from restapi.views import studentoperations
simple_router= SimpleRouter()
simple_router.register("student",studentoperations)
urlpatterns= simple_router.urls