from django.conf.urls import url
from .import views

urlpatterns=[
    url(r'',views.post_list,name='post_list')#views의 post_list를 참조하며, url이름이 post_list가 된다.
]