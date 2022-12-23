"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from myApp import views as BookView
from myApp import cartViews as CartView
from myApp import orderViews as OrderView
from myApp import likeStarView as StarView

from django.urls import re_path
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_book/',BookView.add_book),
    path('show_books/',BookView.show_books),
    path('add_userInfo/',BookView.add_userInfo),
    path('search_userInfo/',BookView.search_userInfo),
    path('fetch_userInfo/',BookView.fetch_userInfo),
    path('edit_userInfo/',BookView.edit_userInfo),
    path('userId2userName/',BookView.userId2userName),
    path('search_usertype/',BookView.search_usertype),

    path('add_product/', BookView.add_product),
    path('show_products/',BookView.show_products),
    path('fetch_product/',BookView.fetch_product),
    path('add_product_stock/',BookView.add_product_stock),
    path('fetch_stock/',BookView.fetch_stock),
    path('show_searched_products/',BookView.show_searched_products),


    path('show_cart/',CartView.show_cart),
    path('add_to_cart/',CartView.add_to_cart),
    path('delete_item_in_cart/',CartView.delete_item_in_cart),
    path('cartProductsList/',CartView.cartProductsList),
    path('edit_num_in_cart/',CartView.edit_num_in_cart),

    path('add_order/',OrderView.add_order),
    path('show_order_products/',OrderView.show_order_products),
    path('show_business_order/',OrderView.show_business_order),
    path('show_customer_order/',OrderView.show_customer_order),
    path('show_business_orderProduct/',OrderView.show_business_orderProduct),
    path('show_customer_orderProduct_status/',OrderView.show_customer_orderProduct_status),
    path('alterOrderStatus/',OrderView.alterOrderStatus),
    path('show_business_orderProduct_status/',OrderView.show_business_orderProduct_status),

    path('get_user_like_to_product/',StarView.get_user_like_to_product),
    path('toggle_user_like_to_product/',StarView.toggle_user_like_to_product),
    path('get_product_likes',StarView.get_product_likes),

    re_path(r'^media/avatar/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT,'avatar/')}),
    re_path(r'^media/user_avatar/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT,'user_avatar/')}),
    re_path(r'^media/comments/(?P<path>.*)$', serve, {'document_root': os.path.join(settings.MEDIA_ROOT,'user_avatar/')}),

    #re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path("",TemplateView.as_view(template_name="index.html"))
]
