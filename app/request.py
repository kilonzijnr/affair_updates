from typing import SupportsRound
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

def get_sources():
    """
    gets json responses from the api.
    """
    get_sources_url = sources_base_url.format(api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        Sources_results = None

        if get_sources_response["sources"]:
            Sources_results_list = get_sources_response["sources"]
            Sources_results = process_results_sources(Sources_results_list)
    return Sources_results

def process_result_sources(sources_list):
    """
    A function to process the sources response and turn into list of objects
    """
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get("id")
        name = sources_item.get("name")
        description = sources_item.get("description")
        url =sources_item.get("url")

        sources_object = Sources(id, name, description, url)

        sources_results.append(sources_object)
    
    return sources_results


def get_articles(source_id):
    """
    Function that gets the json response to our url request
    """
    get_articles_url = articles_base_url.format(source_id, api_key)
    
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_result = None

        if get_articles_response["articles"]:
            articles_result_list = get_articles_response["articles"]
            articles_result = process_result_sources(articles_result_list)
    
    return articles_result

def process_results_articles(articles_list):
    """
    Process articles results and turns them to a list of objects
    """
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get("author")
        title = articles_item.get("title")
        description = articles_item.get("description")
        url = articles_item.get("url")
        urlToImage = articles_item.get("urlToImage")
        publishedAt = articles_item.get("publishedAt")

        articles_objects = Articles(author, title, description, url, urlToImage, publishedAt)

        articles_results.append(articles_objects)

    return articles_results


