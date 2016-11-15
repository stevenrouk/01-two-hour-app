from django.conf.urls import url, include

from blog import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add-post$', views.add_post, name='add-post'),
    url(r'^post-detail/([0-9]+)/$', views.post_detail, name='post-detail'),
]
