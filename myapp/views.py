from django.shortcuts import render
from django.views.generic import DetailView, ListView
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
        context["title"] = Blog.title # titleを表示
        context["text"] = Blog.text
        context["created"] = Blog.created
        context["modified"] = Blog.modified
        return context
    
# 登録した記事の一覧を表示する
class BlogListView(ListView):
    model = Blog # 忘れないように
    template_name = "blogs/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Blog.title # titleを表示
        context["text"] = Blog.text
        context["created"] = Blog.created
        context["modified"] = Blog.modified
        context["count"] = Blog.objects.all().count()
        return context