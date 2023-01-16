from django.urls import path
from . import views

urlpatterns = [
    path('', views.addAndShow, name='home'),
    path('updatestudent/<int:id>', views.updateStudent, name='updateStudent'),
    path('delete/<int:id>/', views.deleteStudent, name='deleteStudent')
]
