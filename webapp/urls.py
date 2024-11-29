from django.urls import path
from webapp import views
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('about_page/', views.about_page, name="about_page"),
    path('contact_page/', views.contact_page, name="contact_page"),
    path('save_contact/', views.save_contact, name="save_contact"),
    path('product_page/', views.product_page, name="product_page"),
    path('products_filtered/<cat_name>/', views.products_filtered, name="products_filtered"),
    path('single_product/<int:single_id>/', views.single_product, name="single_product"),
    path('sign_up/',views.sign_up,name="sign_up"),
    path('', views.sign_in, name="sign_in"),
    path('save_signup/',views.save_signup,name="save_signup"),
    path('user_login/',views.user_login,name="user_login"),
    path('user_logout/',views.user_logout,name="user_logout"),
    path('save_cart/', views.save_cart, name="save_cart"),
    path('cart_page/', views.cart_page, name="cart_page"),
    path('checkout/', views.checkout, name="checkout"),
    path('save_check/', views.save_check, name="save_check"),
    path('payment_page/',views.payment_page,name='payment_page'),
]