from django.urls import path


from .views import index_view,Pictures_Anonymous_Api,Pictures_Create_Api,Pictures_List_Create_Api,Pictures_Delete_View,Pictures_Filter_View

from rest_framework import routers

from django.conf import settings
from django.urls import re_path
from django.views.static import serve


router = routers.SimpleRouter()


urlpatterns = [
    path('hello/', index_view, name='hello'),
    path('picture_any_user/', Pictures_Anonymous_Api.as_view(),
      name='pictures-anonymous'),
    path('picture_create/', Pictures_Create_Api.as_view(),
      name='pictures-create'),
    path('picture_list_create/', Pictures_List_Create_Api.as_view(),
    name='pictures-list-create'),
    path('picture_delete/', Pictures_Delete_View.as_view(),
    name='pictures-delete'),
    path('picture_filter/', Pictures_Filter_View.as_view(),
    name='pictures-filter'),
]
urlpatterns += router.urls