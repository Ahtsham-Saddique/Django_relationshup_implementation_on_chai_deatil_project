
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.all_temp,name="all_temp"),
    path('<int:chai_id>/', views.chai_details,name="chai_detail"),
    

]