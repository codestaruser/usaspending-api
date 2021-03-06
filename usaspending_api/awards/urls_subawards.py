from django.conf.urls import url

from usaspending_api.awards import views

# map reqest types to viewset method; replace this with a router
subaward_list = views.SubawardViewSet.as_view({
    'get': 'list', 'post': 'list'})
subaward_detail = views.SubawardViewSet.as_view({
    'get': 'retrieve', 'post': 'retrieve'})
subaward_total = views.SubawardAggregateViewSet.as_view({
    'get': 'list', 'post': 'list'})

urlpatterns = [
    url(r'^$', subaward_list, name='subaward-list'),
    url(r'(?P<pk>[0-9]+)/$', subaward_detail, name='subaward-detail'),
    url(r'^autocomplete/', views.SubawardAutocomplete.as_view()),
    url(r'^total/', subaward_total, name='subaward-total')
]
