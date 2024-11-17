"""
URL configuration for library_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from users import views as user_views
from django.contrib.admin.models import LogEntry

from django.conf import settings
from django.conf.urls.static import static

# Custom admin view
# def custom_admin_index(request):
#     print("AAAAAAAAAAA")
#     recent_actions = LogEntry.objects.all().order_by('-action_time')[:10]
#     return render(request, 'admin/index.html', {'recent_actions': recent_actions})

# def custom_admin_index(request):
#     # Add custom logic here (if needed)
#     return site.index(request)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    # path('', user_views.home_page, name='home_page'), # maps the root URL (/) to your home page view.
    path('', user_views.home_page, name='home_page'),
    # path('admin/', custom_admin_index, name='custom_admin_index'),
    # path('', include('users.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)