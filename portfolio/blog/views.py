from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from .models import Post
from django.urls import reverse_lazy


class HomePageView(ListView):
    model = Post
    template_name = "home.html"


class DetailPageView(DetailView):
    model = Post
    template_name = "detail.html"


class BlogCreateView(CreateView):
    model = Post
    template_name = "create.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "update.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "delete.html"
    success_url = reverse_lazy("home")
