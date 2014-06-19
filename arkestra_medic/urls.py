from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # admin and admindocs
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # core Arkestra
    url(r'^semantic/', include('semanticeditor.urls')),
    url(r"", include("contacts_and_people.urls")),
    url(r"", include("links.urls")),

    # Arkestra publications
    url(r"", include("publications.urls")),

    # Arkestra clinical studies
    url(r'', include('arkestra_clinical_studies.urls')),

    # Form designer
    url(r'^forms/', include('form_designer.urls')),

    # Javascript internationalisation
    url(
        r'^jsi18n/(?P<packages>\S+?)/$',
        'django.views.i18n.javascript_catalog'
        ),

    # widgetry autocomplete
    url('^autocomplete/$', 'widgetry.views.search', name='widgetry-search'),
    )

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#redirect patterns must come before cms catch-all
urlpatterns += patterns('django.views.generic.simple',
    url(r'^pgt/', 'redirect_to', {'url':'/graduate-studies/',}),
)

# django CMS gets everything else
urlpatterns += patterns('',
    url(r'^', include('cms.urls')),
)
