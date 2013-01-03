from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),

    (r'^admin/doc/', include('django.contrib.admindocs.urls')),                                   
    
    (r'^admin/', include(admin.site.urls)),
    
    (r'^semantic/', include('semanticeditor.urls')),
    (r"", include("contacts_and_people.urls")),

    (r"", include("publications.urls")),
        
    
    (r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
)

# if settings.DEBUG:
#     urlpatterns+= patterns('',
#         url(r'^media/cms/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.CMS_MEDIA_ROOT, 'show_indexes': True}),
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
#     )
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
#redirect patterns must come before cms catch-all   
urlpatterns += patterns('django.views.generic.simple',
    (r'^pgt/', 'redirect_to', {'url':'/graduate-studies/',}),
)
 
urlpatterns += patterns('',
    url('^autocomplete/$', 'widgetry.views.search', name='widgetry-search'),
    url(r'^', include('cms.urls')),
)