from django.shortcuts import render

class VenueListView(ListView):
    model = Venue

    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset.filter(draft=False).filter(is_exam=True)


class VenueDetailView(DetailView):
    model = Quiz
    slug_field = 'url'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.is_exam:
            raise PermissionDenied

        if self.object.draft and not request.user.has_perm('quiz.change_quiz'):
            raise PermissionDenied

        if self.object.login_required and not request.user.is_authenticated():
            return render(request, 'single_complete.html')

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

