from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Garage control",
      default_version='v1',
      description="Application to control electricity consumption",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
   re_path(
      'swagger(?P<format>\.json|\.yaml)$',
      schema_view.without_ui(cache_timeout=0),
      name='schema-json'
   ),
   path(
      'docs/',
      schema_view.with_ui('swagger', cache_timeout=0),
      name='schema-swagger-ui'
   ),
   path(
      'redoc/',
      schema_view.with_ui('redoc', cache_timeout=0),
      name='schema-redoc'
   ),
]