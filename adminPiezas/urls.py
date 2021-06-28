from django.urls import  path
from .views import home, editForm

urlpatterns = [
    path('', home, name='home'),
    path('edit-pieza/<nro>', editForm, name='edit-pieza' )
]