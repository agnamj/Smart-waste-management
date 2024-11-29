from django.urls import path
from Adonaiapp import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('add_category/',views.add_category,name="add_category"),
    path('save_date/',views.save_date,name="save_date"),
    path('display_category/', views.display_category, name="display_category"),
    path('edit_category/<int:cat_id>/', views.edit_category, name="edit_category"),
    path('update_category/<int:cat_id>/', views.update_category, name="update_category"),
    path('delete_category/<int:cat_id>/', views.delete_category, name="delete_category"),

    path('product/', views.product, name="product"),
    path('save_pro/', views.save_pro, name="save_pro"),
    path('display_product/',views.display_product,name="display_product"),
    path('edit_product/<int:pro_id>/', views.edit_product, name="edit_product"),
    path('update_product/<int:pro_id>/', views.update_product, name="update_product"),
    path('delete_product/<int:pro_id>', views.delete_product, name="delete_product"),

    path('loginpage/', views.loginpage, name="loginpage"),
    path('admin_page/', views.admin_page, name="admin_page"),
    path('admin_logout/', views.admin_logout, name="admin_logout"),
    path('display_contact/', views.display_contact, name="display_contact"),
    path('delete_contact/<int:con_id>/', views.delete_contact, name="delete_contact"),

]