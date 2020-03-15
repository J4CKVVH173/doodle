import requests
from googlesearch import search
from bs4 import BeautifulSoup


def search_and_parsing(query: str) -> dict:
    """Метод для запроса данных по query и парсинга данных по найденным сайтам."""
    result_of_search = dict()
    description = 'description'
    title = 'title'
    for url in search(query,  # The query you want to run
                      tld='com',  # The top level domain
                      lang='ru',  # The language
                      num=15,  # Number of results per page
                      start=0,  # First result to retrieve
                      stop=15,  # Last result to retrieve
                      pause=0,  # Lapse between HTTP requests
                      ):
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, features="html.parser")
            metas = soup.find_all('meta')
            result_of_search[url] = dict()
            for meta in metas:
                if 'name' in meta.attrs and meta.attrs['name'] == description:
                    d = result_of_search[url].get(description, [])
                    d.append(meta.attrs['content'])
                    result_of_search[url][description] = d
                if 'name' in meta.attrs and meta.attrs['name'] == title:
                    t = result_of_search[url].get(title, [])
                    t.append(meta.attrs['content'])
                    result_of_search[url][title] = t
        except Exception as e:
            print(e)
    return result_of_search
