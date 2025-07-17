from django.urls import path
from . import views



urlpatterns = [
    path('insert/', views.add_academic_year , name="insert" ),
    path('show/<str:id>/', views.get_academic_year , name="show" ),
    path('update/<str:id>/', views.update_academic_year , name="update" ),
    path('disable/<str:id>/', views.disable_academic_year , name="delete" )

]
