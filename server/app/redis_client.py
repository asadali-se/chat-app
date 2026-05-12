import redis
from app.config import settings

# Create Redis connection
redis_client = redis.from_url(
    settings.redis_url,
    encoding="utf-8",
    decode_responses=True
)


def get_redis():
    """
    Dependency function to get Redis client.
    Use this in FastAPI endpoints with Depends(get_redis)
    """
    return redis_client


# Helper functions for common Redis operations
def set_key(key: str, value: str, expire_seconds: int = None):
    """Set a key-value pair in Redis, optionally with expiration"""
    return redis_client.set(key, value, ex=expire_seconds)


def get_key(key: str):
    """Get a value by key from Redis"""
    return redis_client.get(key)


def delete_key(key: str):
    """Delete a key from Redis"""
    return redis_client.delete(key)


def exists_key(key: str) -> bool:
    """Check if a key exists in Redis"""
    return redis_client.exists(key) > 0