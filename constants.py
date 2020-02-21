"""Constants (a.k.a. macros)"""
import re

# For Mongo DB
MONGO_URI = "mongodb+srv://nicholasbarreyre:zbYKVIASLhvZI3OC@csci4145-5m4ga.azure.mongodb.net/test?retryWrites=true&w=majority"

# For external api
WEATHER_BASE_URL = 'https://api.darksky.net/forecast'
WEATHER_APP_ID = 'cfb1cb0b2ada3699f6f838811969d34d'
HALIFAX_LAT = str(44.64249)
HALIFAX_LONG = str(-63.5718)

# For postal code validation
POSTAL_CODE_PATTERN = re.compile('^[A-Z]\d[A-Z]\d[A-Z]\d$')