from decouple import config

print(f"SECRET_KEY: {config('SECRET_KEY')}")
print(f"DEBUG: {config('DEBUG', default=False, cast=bool)}")
print(f"DB_NAME: {config('DB_NAME')}")
print(f"DB_USER: {config('DB_USER')}")
print(f"DB_PASSWORD: {config('DB_PASSWORD')}")
print(f"DB_HOST: {config('DB_HOST')}")
print(f"DB_PORT: {config('DB_PORT')}")

