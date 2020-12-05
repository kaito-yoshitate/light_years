from django.urls import path
from gravitation import views

app_name = 'gravitation'
urlpatterns = [
    path('gravitation/register', views.register_user,          name='register'),
    path('gravitation/',         views.display_prev_lonliness, name='someone'),
    path('gravitation/submit/',  views.submit_own_lonliness,   name='mine')
]
