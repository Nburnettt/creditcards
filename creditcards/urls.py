from django.urls import path

from .views import index

urlpatterns = [
    # path('', IndexView.as_view(), name='index')
    path('', index, name='redirect_view'),
    path('cards/', index, name='index')
]