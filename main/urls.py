from django.conf.urls import url
from views import IndexView, ZOEhubView, ZOEaiView, UsesView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^zoehub$', ZOEhubView.as_view(), name='zoehub'),
    url(r'^zoeai$', ZOEaiView.as_view(), name='zoeai'),
    url(r'^uses$', UsesView.as_view(), name='uses'),
    url(r'^buy$', IndexView.as_view(), name='buy')
]