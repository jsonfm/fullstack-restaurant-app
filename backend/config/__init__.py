from dotenv import dotenv_values

env = dotenv_values("../.env")

config = {
    "DB_HOST": env.get("DB_HOST", ""),
    "DB_PORT": env.get("DB_PORT", 5432),
    "DB_NAME": env.get("DB_NAME", ""),
    "DB_USER": env.get("DB_USER", ""),
    "DB_PASSWORD": env.get("DB_PASSWORD", ""),
}