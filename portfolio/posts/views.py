from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class AboutPageView(ListView):
    model = Post
    template_name = 'about.html'