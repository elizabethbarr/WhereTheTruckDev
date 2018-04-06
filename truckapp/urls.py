"""truckapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from app.views import IndexView,SignUpView,LoginView,LogoutView,VendorListingCreateView,VendorListView,RSSfeedView,PrivacyDoc
from django.conf.urls.static import static
from django.conf import settings
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^signup/$', SignUpView.as_view(), name='sign_up_view'),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^vendor_listing_create/$', VendorListingCreateView.as_view(), name='vendor_listing_create_view'),
    url(r'^rss_feed/$', RSSfeedView.as_view(), name='rss_feed_view'),
    url(r'^vendor_list/$', VendorListView.as_view(), name='vendor_list_view'),
    url(r'^privacy/$', PrivacyDoc.as_view(), name='privacy_view')


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
