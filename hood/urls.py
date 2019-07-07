from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^profile/(\d+)', views.profile, name='profile'),
    url(r'^update/profile/(\d+)$', views.update_profile, name='update-profile'),
    url(r'^join/(\d+)$', views.join, name='join'),
    url(r'^neighborhood/(\d+)$', views.neighborhood, name='neighborhood'),
    url(r'^business/(\d+)$', views.business, name='business'),
    url(r'^add/business/(\d+)$', views.add_business, name='add-business'),
    url(r'^post/(\d+)$', views.post, name='post'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)