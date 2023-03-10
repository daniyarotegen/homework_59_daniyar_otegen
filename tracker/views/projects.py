from django.views.generic import TemplateView, CreateView

from tracker.models import Project


class ProjectIndexView(TemplateView):
    template_name = 'projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.order_by('start_date')
        return context


