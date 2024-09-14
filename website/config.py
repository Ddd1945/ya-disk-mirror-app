from .scripts.helpers.network import get_local_ip

APP_MODE = 'dev'  # dev | prod

APP_HOST = '127.0.0.1'
APP_PORT = 5000

NGINX_HOST = get_local_ip()
NGINX_PORT = 443

DEBUG = True
USE_RELOADER = True

THREADS = 100

DB_NAME = 'database.db'

SECRET_KEY = '9EH6rk8YIQwGGeOZQORjifn5ikCCwswDxJ+5MFDBAwM='
