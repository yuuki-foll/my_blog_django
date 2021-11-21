from django.urls import path
from . import views
from myapp.views import BlogDetailView, BlogListView    # View追加


# pathの引数について
# route, view, kwargs, name
urlpatterns = [
     path('list/',BlogListView.as_view(),name="list"), # View追加
     path('detail/<slug:pk>/',BlogDetailView.as_view(),name="detail"), # View追加
     path('',views.index, name='index'),
]