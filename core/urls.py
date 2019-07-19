from django.urls import path

from .views import homePageView, ProjectPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('projects', ProjectPageView, name='projects'),
]
