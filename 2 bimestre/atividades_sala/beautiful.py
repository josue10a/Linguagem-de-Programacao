import requests
from bs4 import BeautifulSoup

def google_search(query, num_results=5):
    #Formata a URL da pesquisa no Google
    