from django.shortcuts import render
from django.views.generic import DetailView
from myapp.models import Blog

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

class BlogDetailView(DetailView):
    model = Blog # 忘れないように
    template_name = "blogs/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "MyPage"
        return context
    