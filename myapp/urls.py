from django.urls import path
from . import views


# pathの引数について
# route, view, kwargs, name
urlpatterns = [
     path('',views.index, name='index'),
]