from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('wishlist', views.wishlist.as_view(), name='wishlist'),
    path('returnsAndOrders', views.returnsAndOrders.as_view(), name='returnsAndOrders'),
    path('detailPage', views.detailPage.as_view(), name='detailPage'),
    path('customerInfo', views.customerInfo.as_view(), name='customerInfo'),
    path('contactUs', views.contactUs.as_view(), name='contactUs'),
    path('cart', views.cart.as_view(), name='cart'),
    path('blogDetail', views.blogDetail.as_view(), name='blogDetail'),
    path('allColumns', views.allColumns.as_view(), name='allColumns'),
]
