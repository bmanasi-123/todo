from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup),
    path('login/',views.loginn),
    path('home/',views.todo),
    path('edit_todo/<int:id>/',views.todo_update),
    path('delete_todo/<int:id>/',views.todo_delete),
    path('signout/',views.signout,name='signout'),
]
