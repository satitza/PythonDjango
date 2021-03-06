from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('add/<int:id>/<str:name>', views.Add, name='add'),
    path('page', views.Page, name='page'),
    path('register', views.Register, name='register'),
    path('content', views.Content, name='content')
]
