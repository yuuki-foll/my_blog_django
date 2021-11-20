"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # include追加
from django.conf.urls import url # markdown追加
from django.conf.urls.static import static #markdown追加
from django.conf import settings    #markdown追加

urlpatterns = [
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    #url(r'mdeditor/',include('mdeditor.urls')) #markdown追加
    path('markdownx/',include('markdownx.urls')) #markdown追加
]

#markdown追加
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

#markdown追加
""" if settings.DEBUG:
    # static files (images, cssm javascript etc)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # """