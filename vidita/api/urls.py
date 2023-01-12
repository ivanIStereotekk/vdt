from django.urls import path


from .views import index_view,Pictures_Anonymous_Api,Pictures_Create_Api,Pictures_List_Create_Api,Pictures_Delete_View,Pictures_Filter_View

from rest_framework import routers

from django.conf import settings
from django.urls import re_path
from django.views.static import serve


router = routers.SimpleRouter()


urlpatterns = [
    path('hello/', index_view, name='hello'),
    path('pictures_any_user/', Pictures_Anonymous_Api.as_view(),
      name='pictures-anonymous'),
    path('pictures_create/', Pictures_Create_Api.as_view(),
      name='pictures-create'),
    path('pictures_list/', Pictures_List_Create_Api.as_view(),
    name='pictures-list'),
    path('pictures_delete/', Pictures_Delete_View.as_view(),
    name='pictures-delete'),
    path('pictures_filter/', Pictures_Filter_View.as_view(),
    name='pictures-filter'),
]
urlpatterns += router.urls