from django.urls import path
from authentication.views import login
from authentication.views import login, register  # Tambahkan register di baris ini


app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]