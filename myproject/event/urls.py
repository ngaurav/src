from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import VenueListView, VenueDetailView

urlpatterns = patterns('',
                       url(regex=r'^$',
                           view=VenueListView.as_view(),
                           name='venue_list'),
)
