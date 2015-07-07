from django.conf.urls import include, url
from productapp.views import login
from productapp.views import signup
from productapp.views import dashboard
from productapp.views import logout
from productapp.views import profile
from productapp.views import addcategory,subcategory,addproduct,showproduct,delete_product,not_found,search

urlpatterns = [
    
    url(r'^login/$',login),
    url(r'^signup/$', signup),
    url(r'^dashboard/$',dashboard),
    url(r'^logout/$',logout),
    url(r'^dashboard/profile/$',profile),
    url(r'^dashboard/addcategory/(\d+)/$',addcategory),
    url(r'^dashboard/0$',dashboard),
    url(r'^dashboard/([\d+/]+)$',subcategory),
    url(r'^/*$', login),
    url(r'^dashboard/addproduct/$',addproduct),
    url(r'^dashboard/search/$',search),
    url(r'^dashboard/products/(\d+)/$',showproduct),
    url(r'^dashboard/products/delete/(\d+)/$',delete_product),
    url(r'^.*/$',not_found),
    


]