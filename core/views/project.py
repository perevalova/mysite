from django.views.generic import TemplateView


class ProjectPageView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = {'studaccservice': 'https://studaccservice.herokuapp.com'}

        return context
