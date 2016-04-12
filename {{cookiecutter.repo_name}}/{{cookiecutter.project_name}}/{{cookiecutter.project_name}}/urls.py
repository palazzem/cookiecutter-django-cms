from django.conf.urls import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.views.generic.base import TemplateView

from cms.sitemaps import CMSSitemap


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]


urlpatterns += i18n_patterns(
    url(r'^bad/$', bad),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^django-rq/', include('django_rq.urls')),
    {% if cookiecutter.extra_plugins == "y" or cookiecutter.extra_plugins == "Y" %}
    url(r'^select2/', include('django_select2.urls')),
    {% endif %}
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
        url(r'^500/$', TemplateView.as_view(template_name='500.html'), name='500'),
    ]

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
