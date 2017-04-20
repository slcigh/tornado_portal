import os
import config
import routes

DEBUG = True
PORT = 8899
ROUTES = routes.ROUTES

DATABASE = {
    'NAME': config.DB_NAME,
    'USER': config.DB_USER,
    'PASSWORD': config.DB_PASSWORD,
    'HOST': config.DB_HOST,
    'PORT': int(config.DB_PORT),
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
