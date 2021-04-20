from django.views.generic import ListView, DetailView
from . models import News

class NewsListView(ListView):
    model = News
    template_name = 'home.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'detail.html'