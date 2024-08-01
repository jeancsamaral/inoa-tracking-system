# File: inoa_tracking/stocks/urls.py
from django.urls import path
from . import views
from stocks.send_email import send_email
from stocks.views import send_alert_email

urlpatterns = [
    path('api/stocks/add/', views.add_stock, name='add-stock'),
    path('stocks/delete/<str:symbol>/', views.delete_stock, name='delete_stock'),
    path('api/stocks/', views.stock_data_view, name='stock_data_view'),
    path('', views.stock_list, name='stock_list'),
    path('email/', send_email, name="send_email"),
    path('api/send-email/', send_alert_email, name='send_alert_email'),
]
