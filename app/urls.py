from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import core.views.example
import core.views.book_search


urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-search/', core.views.book_search.book_search),
    path('example/', core.views.example.example),
] + staticfiles_urlpatterns()
