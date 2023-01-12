from django.urls import path


from .views import index_view,Pictures_Anonymous_Api

from rest_framework import routers

from django.conf import settings
from django.urls import re_path
from django.views.static import serve


router = routers.SimpleRouter()


urlpatterns = [
    path('hello/', index_view, name='hello'),
    path('picture_any_user/', Pictures_Anonymous_Api.as_view(),
      name='pictures-anonymous'),
]
urlpatterns += router.urls