from django.shortcuts import render
from .models import Venue
from django.views.generic import DetailView, ListView, TemplateView

class VenueListView(ListView):
    context_object_name = 'venues'
    template_name = 'home.html'

    def get_queryset(self):
        return Venue.objects.filter(featured=True)


class VenueDetailView(DetailView):
    model = Venue
    slug_field = 'our_id'
    context_object_name = 'venue'
    template_name = 'venue.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

