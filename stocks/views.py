from django.http import JsonResponse
from .models import Stock
from .serializers import StockSerializer
from rest_framework import generics, status
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
import requests
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from datetime import datetime, timedelta
import json
from stocks.send_email import send_email

class StockListAPIView(generics.ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

@csrf_exempt
def send_alert_email(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            subject = data.get('subject', 'Stock Alert')
            message = data.get('message', '')
            recipient_list = data.get('recipient_list', [])

            # Adicionando logs para verificação
            print(f"Subject: {subject}")
            print(f"Message: {message}")
            print(f"Recipient List: {recipient_list}")
            print(f"Type of recipient_list: {type(recipient_list)}")

            if not isinstance(recipient_list, (list, tuple)):
                return JsonResponse({"error": "Recipient list must be a list or tuple."}, status=400)

            send_email(
                subject,
                message,
                recipient_list,
            )
            return JsonResponse({'status': 'Email sent successfully'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON provided.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@require_http_methods(["DELETE"])
@csrf_exempt
def delete_stock(request, symbol):
    try:
        stock = Stock.objects.get(symbol=symbol)
        stock.delete()
        return JsonResponse({"message": f"Stock {symbol} deleted successfully."}, status=200)
    except Stock.DoesNotExist:
        return JsonResponse({"error": f"Stock {symbol} not found."}, status=404)

@csrf_exempt
@api_view(['POST'])
@permission_classes([AllowAny])  # Allow any request without permission checks
def add_stock(request):
    symbol = request.data.get('symbol')
    upper = request.data.get('upper')
    lower = request.data.get('lower')
    frequency = request.data.get('frequency')

    if not symbol or upper is None or lower is None or frequency is None:
        return Response({"error": "Symbol, upper, lower, and frequency are required."}, status=400)
    
    price_data = fetch_stock_data(symbol)
    if price_data:
        stock, created = Stock.objects.update_or_create(
            symbol=symbol,
            defaults={'price': price_data['price'], 'upper': upper, 'lower': lower, 'frequency': frequency}
        )
        return JsonResponse({'symbol': stock.symbol, 'price': stock.price, 'upper': stock.upper, 'lower': stock.lower, 'frequency': stock.frequency}, status=201)
    else:
        return Response({"error": "Failed to fetch stock data."}, status=400)

def stock_data_view(request):
    symbols = ['TSLA']
    stock_data_list = []

    for symbol in symbols:
        data = fetch_stock_data(symbol)
        if data:
            stock_data_list.append(data)
            Stock.objects.update_or_create(
                symbol=symbol,
                defaults={'price': data['price']}
            )

    return JsonResponse({'stocks': stock_data_list})

def fetch_stock_data(symbol):
    api_key = 'FToQA2DNCCtJgEYHVpAUXhqGNACMp1nB'
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/prev?apiKey={api_key}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'results' in data and data['results']:
            latest_data = data['results'][0]
            return {
                'symbol': symbol,
                'price': latest_data['c'],  # 'c' for closing price
                'timestamp': latest_data['t']
            }
    except requests.RequestException as e:
        print(f"HTTP Request failed for {symbol}: {e}")
    return None

def stock_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/stock_list.html', {'stocks': stocks})

def fetch_400_days_data(symbol):
    api_key = 'FToQA2DNCCtJgEYHVpAUXhqGNACMp1nB'
    end_date = datetime.today()
    start_date = end_date - timedelta(days=400)
    url = f'https://api.polygon.io/v2/aggs/ticker/{symbol}/range/1/day/{start_date.strftime("%Y-%m-%d")}/{end_date.strftime("%Y-%m-%d")}?apiKey={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if 'results' in data:
            prices = [result['c'] for result in data['results']]  # Extracting the closing prices
            # Update or create the Stock entry
            stock, created = Stock.objects.update_or_create(
                symbol=symbol,
                defaults={'price': prices[-1], 'price_history': prices}
            )
            return prices
        else:
            print(f"No data found for {symbol}")
            return []
    except requests.RequestException as e:
        print(f"HTTP Request failed for {symbol}: {e}")
        return []

