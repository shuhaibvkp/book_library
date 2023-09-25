from django.urls import path
from .views import *

urlpatterns=[

    path('index/',index.as_view(), name='index'),
    path('authregisterclass/', authregisterclass.as_view(), name='authregisterclass'),
    path('profile/<pk>',profile.as_view(),name='profile'),
    path('bookdelete/<pk>', bookdelete.as_view(),name='bookdelete' )
]