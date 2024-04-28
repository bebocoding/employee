from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_host: str = "dpg-con9inocmk4c73a1g1u0-a.oregon-postgres.render.com"
    database_port: str = "5432"
    database_password: str = "YfEzm6rG60JZVREXj3EnCDbuayu0uMsr"
    database_name: str = "bebo"
    database_username: str = "bebo"
    secret_key: str = "kasldgjklsdjglskdjklsad62s1ad56ga"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 500


settings = Settings()
