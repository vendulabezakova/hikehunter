from django.shortcuts import render

from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DetailView
import hikehunter.models as models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from hikehunter.forms import HikeForm, RegisterUserForm
from hikehunter.forms import RegisterUserForm, HikeForm
from .filters import HikeFilter
import hikehunter.tables as tables
from django_tables2 import SingleTableView


class IndexView(TemplateView):
    template_name = "index.html"


class HikeCreateView(CreateView):
    model = models.Hike
    template_name = "create_hike.html"
    fields = ["name", "region", "difficulty", "length", "peak", "terrain", "lowestpoint"]
    success_url = reverse_lazy("index")

class HikeListView(ListView):
    model = models.Hike
    template_name = "hike_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = HikeFilter(self.request.GET, queryset=self.get_queryset())
        return context

class HikeCreateView(LoginRequiredMixin, CreateView):
    form_class = HikeForm
    template_name = "create_hike.html"
    success_url = reverse_lazy("index")
    success_message = _("Hike was created")

class HikeDetailView(DetailView):
    model = models.Hike
    template_name = "hike_detail.html"

class RegisterView(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"