# track-config/urls.py
from django.contrib import admin
from django.urls import path, include
from stocks.views import StockListAPIView, stock_data_view
from stocks.views import stock_list
from stocks.views import delete_stock
from stocks.views import add_stock
from stocks.send_email import send_email
from stocks.views import send_alert_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocks/', stock_data_view),  # Ensure this matches the function name in views.py
    path('api/stocks/', StockListAPIView.as_view(), name='api_stocks'),
    path('stocks/delete/<str:symbol>/', delete_stock, name='delete_stock'),
    path('api/stocks/add/', add_stock, name='add-stock'),
    path('email/', send_email, name="send_email"),
    path('', stock_list, name='stock_list'),
    path('api/send-email/', send_alert_email, name='send_alert_email'),
]
