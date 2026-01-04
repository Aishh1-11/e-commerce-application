from django.urls import path
from AdminApp import views

urlpatterns = [

    path("dashboard/",views.dashboard,name="dashboard"),
    path("add_category/",views.add_category,name="add_category"),
    path("save_category/", views.save_category, name="save_category"),
    path("edit_category/<int:category_id>/", views.edit_category, name="edit_category"),
    path("update_category/<int:category_id>/", views.update_category, name="update_category"),
    path("delete_category/<int:category_id>/", views.delete_category, name="delete_category"),
    path("display_categories/", views.display_categories, name="display_categories"),


    path("add_product/",views.add_product,name="add_product"),
    path("save_product/",views.save_product,name="save_product"),
    path("display_products/",views.display_products,name="display_products"),
    path("edit_product/<int:product_id>",views.edit_product,name="edit_product"),
    path("update_product/<int:product_id>",views.update_product,name="update_product"),
    path("delete_product/<int:product_id>",views.delete_product,name="delete_product"),

    path("admin_login_page/",views.admin_login_page,name="admin_login_page"),
    path("admin_login/",views.admin_login,name="admin_login"),
    path("admin_logout/",views.admin_logout,name="admin_logout"),







]