from django.urls import path

from users import views
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('upload_document/', views.upload_document, name='upload_document'),

]