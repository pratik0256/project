from django.urls import path
from .views import upload_file

# from django.urls import path
from .views import user_login, register
from django.contrib.auth import views as auth_view


urlpatterns = [
    path('upload_csv/', upload_file, name='upload_csv'),
    # path('match_products', match_products, name='match_products'),
   
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('home/',auth_view.LogoutView.as_view(template_name="myapp/upload_csv.html"),name='upload'),
    path('upload/',auth_view.LogoutView.as_view(template_name="myapp/upload.html"),name='upload'),
    path('index2/',auth_view.LogoutView.as_view(template_name="index.html"),name='index2'),
    path('index/',auth_view.LogoutView.as_view(template_name="index.html"),name='base'),
    
    
]

