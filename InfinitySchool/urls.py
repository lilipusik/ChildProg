from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from school.views import index, catalog, course_detail, toggle_like, send_review, code_checker, all_reviews

admin.site.site_header = "INFINITY CODE"
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', index, name='index'),
    path('users/', include('users.urls', namespace='users')),
    path('catalog/', catalog, name='catalog'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
    path('toggle-like/<int:course_id>/', toggle_like, name='toggle_like'),
    path('send_review/', send_review, name='send_review'),
    path('task/', code_checker, name='task'),
    path('all_reviews/', all_reviews, name='all_reviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
