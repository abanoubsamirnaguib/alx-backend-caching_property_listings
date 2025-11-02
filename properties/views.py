from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property
from .utils import get_all_properties

# Create your views here.

@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    """
    API endpoint to return all properties.
    Response is cached in Redis for 15 minutes.
    Uses low-level caching for the queryset via get_all_properties().
    """
    properties = get_all_properties()
    
    # Convert properties to JSON-serializable format
    properties_data = []
    for property in properties:
        properties_data.append({
            'id': property.id,
            'title': property.title,
            'description': property.description,
            'price': str(property.price),  # Convert Decimal to string for JSON
            'location': property.location,
            'created_at': property.created_at.isoformat(),
        })
    
    return JsonResponse({
        'properties': properties_data,
        'count': len(properties_data)
    })