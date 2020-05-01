from django.urls import path
from . import views
urlpatterns=[

    path('',views.reg,name='reg'),
    path('customer/',views.reg,name='reg'),
    path('submit/',views.submit,name='submit'),
    path('purchase/',views.buy,name='buy'),
    path('click/',views.click,name='click')
    
]