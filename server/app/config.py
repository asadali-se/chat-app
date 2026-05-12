from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    database_url: str
    redis_url: str
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    upload_dir: str = "./uploads"
    max_file_size: int = 5242880  # 5MB
    allowed_image_types: str = "image/jpeg,image/png,image/gif,image/webp"
    allowed_file_types: str = "image/jpeg,image/png,image/gif,image/webp,application/pdf"

    frontend_url: str = "http://localhost:3000"

    class Config:
        env_file = ".env"

    @property
    def allowed_image_types_list(self) -> List[str]:
        return [t.strip() for t in self.allowed_image_types.split(",")]

    @property
    def allowed_file_types_list(self) -> List[str]:
        return [t.strip() for t in self.allowed_file_types.split(",")]


settings = Settings()