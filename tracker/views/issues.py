from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, DeleteView, UpdateView
from tracker.forms import IssueForm
from tracker.models import Issue


class AddView(View):
    template_name = 'issue_create.html'

    def get(self, request, *args, **kwargs):
        form = IssueForm()
        return render(request, self.template_name, context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = IssueForm(data=request.POST)
        if not form.is_valid():
            return render(request, self.template_name, context={
                'form': form,
            })
        else:
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)


class DetailView(TemplateView):
    template_name = 'issue_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        if issue.is_deleted:
            raise Http404
        context['issue'] = issue
        if issue.type.exists():
            context['types'] = issue.type.all()
        else:
            context['types'] = []
        return context


class IssueUpdateView(UpdateView):
    template_name = 'issue_update.html'
    form_class = IssueForm
    model = Issue

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    template_name = 'issue_delete.html'
    model = Issue
    success_url = reverse_lazy('index')
