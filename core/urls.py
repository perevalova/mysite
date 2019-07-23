from django.urls import path

from core.views.contact import ContactView
from core.views.cv import CvPageView, download_file
from .views.main import HomePageView, AboutPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contacts', ContactView.as_view(), name='contacts'),
    path('cv', CvPageView.as_view(), name='cv'),
    path('download/cv', download_file, name='download_pdf')
    # path('projects/', ProjectPageView, name='projects'),
]
