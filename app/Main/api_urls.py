from django.urls import path, include

from Receipt.api_methods import run_receipts_calculating

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('apartments/', include('Apartment.api_urls')),
    path('buildings/', include('Building.api_urls')),
    path('receipts/', include('Receipt.api_urls')),
    path('tariffs/', include('Tariff.api_urls')),
    path('water_meters/', include('WaterMeter.api_urls')),
    path('progress/', include('Progress.api_urls')),
    path('run_receipts_calculating/', run_receipts_calculating),
]
