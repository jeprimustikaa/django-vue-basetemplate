from django.contrib import admin
from django.urls import path, re_path, include

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('admin/', admin.site.urls),
    re_path('api/(?P<version>(v1|v2))/', include('polls.urls'))
]
