from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name = 'home'),
    path('gallery',views.gallery,name = 'gallery'),
    path('contact',views.contact,name = 'contact'),
    path('about',views.about,name = 'about'),
    path('auffy',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('create_post',views.create_post,name = 'create_post'),
    path('add_category',views.add_category,name = 'add_category'),
    path('update/<int:id>',views.update,name = 'update'),
    path('delete/<int:id>',views.delete,name = 'delete'),
    path('show_cat',views.show_cat,name = 'show_cat'),
    path('update_cat/<int:id>',views.update_cat,name = 'update_cat'),
    path('delete_cat/<int:id>',views.delete_cat,name = 'delete_cat'),
    path('<str:category_name>',views.cat_detail,name = 'cat_detail'),


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)