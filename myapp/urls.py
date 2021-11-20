from django.urls import path
from . import views
from myapp.views import BlogDetailView    # View追加


# pathの引数について
# route, view, kwargs, name
urlpatterns = [
     path('detail/<int:pk>/',BlogDetailView.as_view(),name="detail"), # View追加
     path('',views.index, name='index'),
]