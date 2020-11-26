from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import core.views.example


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core.views.example.example)
] + staticfiles_urlpatterns()
