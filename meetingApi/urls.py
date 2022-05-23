from django.contrib import admin
from django.urls import path, re_path
from .views import MyTokenObtainPairView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Meetings API",
      default_version='v1',
      description="This is an API the allows requests to create, users, meeting, write minutes for the meetings and upload documents ",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="-"),
      license=openapi.License(name="-"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

 



from rest_framework_simplejwt.views import (
 
    TokenRefreshView,
)

# importing all the views to register them
from meetingApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meetings/', views.meeting_list),
    path('meetings/<int:uid>', views.users_meeting),
    path('meetings/<int:meetingid>/user/<int:uid>', views.users_meeting_update),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
 
]
