from django.urls import path
from . import views

app_name = 'carto'
urlpatterns = [
    # http://www.auberentransition.fr/carto
    path('', views.index, name='index'),
    # http://www.auberentransition.fr/carto/12
    path('<int:pk>/', views.PoiDetailView.as_view(), name='detail'),
    # http://www.auberentransition.fr/carto/contact
    path('contact/', views.contact, name='contact'),
    # http://www.auberentransition.fr/carto/search
    path('search/', views.search, name='search'),
]
