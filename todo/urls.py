from django.urls import path
from . import views


urlpatterns = [
    path('todo/', views.index, name='index'),
    path('todo/add/', views.additem, name='additem'),
    path('del/<int:id>', views.delitem, name='delitem'),
    path('changepassword', views.changepassword, name='changepassword')

]
