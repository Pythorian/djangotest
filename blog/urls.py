from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pagina_inicial, name='pagina_inicial'),
]