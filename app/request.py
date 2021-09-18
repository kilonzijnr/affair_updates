import urllib.request, json
from .models import Sources, Articles

#getting API_key
api_key= None

#source bases URL
sources_base_url = None

#articles base URL
articles_base_url = None

def config_request(app):
    global api_key, sources_base_url, articles_base_url
    api_key = app.config["SOURCES_API_KEY"]
    sources_base_url = app.config["SOURCES_API_BASE_URL"]
    articles_base_url = app.config["ARTICLES_API_BASE_URL"]


