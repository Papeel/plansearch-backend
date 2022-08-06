"""App Settings. """

from environs import Env

env = Env()

# Config
DEBUG = env.bool('DEBUG', True)
HOST = env.str('HOST', '0.0.0.0')
PORT = env.int('PORT', 8000)
WORKERS = env.int('WORKERS', 4)

# MongoDB
MONGODB_URI = env.str('MONGODB_URI', 'mongodb://plansearch-mongo:27017')
MONGODB_NAME = env.str('MONGODB_NAME', '202_tests')