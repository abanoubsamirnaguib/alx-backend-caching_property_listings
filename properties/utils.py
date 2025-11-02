from django.core.cache import cache
from django_redis import get_redis_connection
import logging
from .models import Property

# Set up logger
logger = logging.getLogger(__name__)


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


def get_redis_cache_metrics():
    """
    Retrieve and analyze Redis cache hit/miss metrics.
    
    This function connects to Redis via django_redis, retrieves keyspace_hits
    and keyspace_misses from INFO command, calculates hit ratio, logs metrics
    and returns a dictionary with the metrics.
    
    Returns:
        dict: Dictionary containing cache metrics including hits, misses, and hit ratio
    """
    try:
        # Connect to Redis via django_redis
        redis_connection = get_redis_connection("default")
        
        # Get Redis info containing keyspace statistics
        info = redis_connection.info()
        
        # Extract keyspace_hits and keyspace_misses
        keyspace_hits = info.get('keyspace_hits', 0)
        keyspace_misses = info.get('keyspace_misses', 0)
        
        # Calculate total operations and hit ratio
        total_operations = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total_operations) if total_operations > 0 else 0
        
        # Prepare metrics dictionary
        metrics = {
            'keyspace_hits': keyspace_hits,
            'keyspace_misses': keyspace_misses,
            'total_operations': total_operations,
            'hit_ratio': hit_ratio,
            'hit_ratio_percentage': hit_ratio * 100
        }
        
        # Log metrics
        logger.info(f"Redis Cache Metrics - Hits: {keyspace_hits}, "
                   f"Misses: {keyspace_misses}, "
                   f"Hit Ratio: {hit_ratio:.4f} ({hit_ratio * 100:.2f}%)")
        
        return metrics
        
    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {str(e)}")
        return {
            'keyspace_hits': 0,
            'keyspace_misses': 0,
            'total_operations': 0,
            'hit_ratio': 0,
            'hit_ratio_percentage': 0,
            'error': str(e)
        }