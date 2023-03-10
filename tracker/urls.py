from django.urls import path
from tracker.views.index import IndexView
from tracker.views.issues import DetailView, AddView, UpdateView, IssueDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path("issue/add", AddView.as_view(), name='issue_create'),
    path("issue/<int:pk>", DetailView.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update/', UpdateView.as_view(), name='issue_update'),
    path('issue/<int:pk>/delete/', IssueDeleteView.as_view(), name='issue_delete'),
    path('issue/<int:pk>/confirm_delete/', IssueDeleteView.as_view(), name='confirm_delete'),
]