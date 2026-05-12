from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from app.config import settings


# Create access token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Creates a JWT access token.
    
    Args:
        data: Data to encode in the token (usually {"user_id": 123})
        expires_delta: How long until token expires (optional)
    
    Returns:
        Encoded JWT token string
    """
    to_encode = data.copy()

    # Set expiration time
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)

    # Add expiration to the payload
    to_encode.update({"exp": expire})

    # Encode and return the token
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


# Create refresh token
def create_refresh_token(data: dict):
    """
    Creates a JWT refresh token (longer expiration).
    
    Args:
        data: Data to encode (usually {"user_id": 123})
    
    Returns:
        Encoded JWT refresh token string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=settings.refresh_token_expire_days)
    to_encode.update({"exp": expire})
    to_encode.update({"type": "refresh"})  # Mark as refresh token

    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


# Verify token and extract data
def verify_token(token: str):
    """
    Verifies a JWT token and returns the decoded data.
    
    Args:
        token: The JWT token to verify
    
    Returns:
        Decoded token data (like {"user_id": 123, "exp": 1234567890})
    
    Raises:
        JWTError: If token is invalid or expired
    """
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except JWTError:
        return None