from passlib.context import CryptContext

# Create password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    Hashes a plain text password using bcrypt.
    
    Args:
        password: Plain text password (e.g., "mypassword123")
    
    Returns:
        Hashed password (e.g., "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p...")
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies if a plain password matches the hashed password.
    
    Args:
        plain_password: Password user entered (e.g., "mypassword123")
        hashed_password: Hash stored in database (e.g., "$2b$12$...")
    
    Returns:
        True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)