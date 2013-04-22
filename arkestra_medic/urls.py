from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),                                   
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^semantic/', include('semanticeditor.urls')),
    url(r"", include("contacts_and_people.urls")),

    url(r"", include("publications.urls")),

    url(r'^resources/', include('curated_resources.urls')),        
    url(r'^forms/', include('form_designer.urls')),
    
    url(r'^jsi18n/(?P<packages>\S+?)/$', 'django.views.i18n.javascript_catalog'),
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
    url(r'^pgt/', 'redirect_to', {'url':'/graduate-studies/',}),
)
 
# urlpatterns = patterns('',
#     (r'^forms/', include('form_designer.urls')),
# )

urlpatterns += patterns('',
    url('^autocomplete/$', 'widgetry.views.search', name='widgetry-search'),
    url(r'^', include('cms.urls')),
)