from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRT_KEY:str = "supersecret"
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 30
    REFRESH_TOKEN_EXPIRE_DAYS:int = 7
settings = Settings()     
