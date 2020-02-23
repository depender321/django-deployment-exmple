from django.conf.urls import url,include
from basic_app import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'formpage/',views.formpage,name='formpage'),
    url(r'modelpage/',views.modelpage,name='modelpage'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'special/',views.special,name='special'),
    url(r'^register/$',views.register,name='register')
]
