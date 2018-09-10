from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start, name='start'),
    url(r'^jedi_page$', views.jedi_page, name='jedi_page'),
    url(r'^candidate_page$', views.candidate_page, name='candidate_page'),
    url(r'^candidate_list$', views.candidate_list, name='candidate_list'),
    url(r'^test_task$', views.test_task, name='test_task'),
    url(r'^candidate_list/(?P<pk>\d+)$', views.candidate_detail, name='candidate_detail'),
    url(r'^to_padawan/(?P<pk>\d+)$', views.to_padawan, name='to_padawan')
]