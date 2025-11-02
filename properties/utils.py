from django.core.cache import cache
from .models import Property


def get_all_properties():
    """
    Retrieve all properties with Redis caching.
    
    This function implements low-level caching using Django's cache framework.
    It first checks Redis for cached data, and if not found, fetches from the
    database and stores the result in Redis for 1 hour.
    
    Returns:
        QuerySet: All Property objects from database or cache
    """
    # Check Redis for cached properties
    cached_properties = cache.get('all_properties')
    
    if cached_properties is not None:
        # Return cached data if available
        return cached_properties
    
    # Fetch from database if not in cache
    properties = Property.objects.all()
    
    # Store in Redis cache for 1 hour (3600 seconds)
    cache.set('all_properties', properties, 3600)
    
    return properties