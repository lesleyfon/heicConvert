from django.conf.urls import include, url

from app import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view())
]
