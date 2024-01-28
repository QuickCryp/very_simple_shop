from django.urls import path
from .views import home, detail, catalog

app_name = 'general'
urlpatterns = [
    path('', home, name='home'),
    path('flower/<int:flower_id>/', detail, name='detail'),
    path('catalog/', catalog, name='catalog')
]