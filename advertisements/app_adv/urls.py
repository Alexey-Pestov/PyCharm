from django.urls import path
from .views import index, top_sellers, adv_post, regist, log_in, pro_file

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', adv_post, name='advertisement-post'),
    path('register/', regist, name='register'),
    path('login/', log_in, name='login'),
    path('profile/', pro_file, name='profile')
]