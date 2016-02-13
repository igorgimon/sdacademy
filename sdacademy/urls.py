from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sdacademy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^student_list$', views.student_list, name='student_list'),
    url(r'^student_detail$', views.student_detail, name='student_detail'),
#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^polls/', include('polls.urls', namespace="polls")),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
