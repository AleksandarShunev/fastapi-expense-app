from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    host: str
    user: str
    password: str
    port: int
    database: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()