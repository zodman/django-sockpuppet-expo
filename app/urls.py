from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

import core.views.example
import core.views.book_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('book-search/', core.views.book_search.book_search,
         name='book_search'),
    path('example/', core.views.example.example, name='example'),
] + staticfiles_urlpatterns()
