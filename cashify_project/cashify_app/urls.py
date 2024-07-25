from django.urls import path
from cashify_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('devices/', views.device_list_view, name='device_list'),
    path('devices/create/', views.device_create_view, name='device_create'),
    path('devices/<int:device_id>/', views.device_detail_view, name='device_detail'),
    path('devices/<int:device_id>/add_to_list/', views.add_to_list, name='add_to_list'),
    path('devices/<int:device_id>/remove_from_list/', views.remove_from_list, name='remove_from_list'),  # Add this line
    path('transactions/', views.transaction_view, name='transactions'),
    path('payment/', views.make_payment_view, name='make_payment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
