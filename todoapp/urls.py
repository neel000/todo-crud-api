from django.urls import path

from . views import *

urlpatterns = [
    path('', HomeView.as_view(),name='website_home'),
    path('<int:id>/', StudentView.as_view(),name='student_view'),
]
