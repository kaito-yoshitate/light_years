from django.urls import path
from gravitation import views

app_name = 'gravitation'
urlpatterns = [
    path('register/', views.register_user,          name='register'),
    path('',          views.display_prev_lonliness, name='someone'),
    path('submit/',   views.submit_own_lonliness,   name='mine')
]
