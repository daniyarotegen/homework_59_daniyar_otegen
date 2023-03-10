from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
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
        context['issue'] = issue
        if issue.type.exists():
            context['types'] = issue.type.all()
        else:
            context['types'] = []
        return context


class UpdateView(TemplateView):
    template_name = 'issue_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_update.html', context={'form': form, 'issue': issue})


class DeleteView(View):

    def get(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        context = {'issue': issue}
        return render(request, 'issue_delete.html', context)

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
