from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from recipient.models import Recipient


class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient


class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient


class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    fields = ['email', 'name', 'description']
    success_url = reverse_lazy('recipient:list')

    def form_valid(self, form):
        new_recipient = form.save()
        new_recipient.owner = self.request.user
        new_recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    fields = ['email', 'name', 'description']

    def get_success_url(self):
        return reverse_lazy('recipient:view', kwargs={'pk': self.get_object().id})


class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    success_url = reverse_lazy('recipient:list')
