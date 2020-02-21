from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('<int:id>/',views.singles,name='singles'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('createblog',views.createblog,name='createblog'),
    path('addblog',views.addblog,name='addblog'),
    
]