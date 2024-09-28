import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_gazzetta_news():
    try:
        url = 'https://www.gazzetta.it/Calcio/'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        news = []
        for article in soup.find_all('div', class_='bck-media-news bck-media-news-medium'):
            title = article.find('h3').get_text(strip=True)
            link = article.find('a')['href']
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Usa il timestamp corrente
            news.append({'source': 'Gazzetta', 'title': title, 'link': link, 'timestamp': timestamp})

        return news
    except Exception as e:
        print(f"Errore nel recupero delle notizie da Gazzetta: {e}")
        return []

def get_fantacalcio_news():
    try:
        url = 'https://www.fantacalcio.it/news/calcio-italia/serie-a'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        news = []
        articles = soup.find_all('article', class_='article-card article-card-03')
        for article in articles:
            title = article.find('h2').get_text(strip=True)
            link = article.find('a')['href']
            if not link.startswith('https'):
                link = 'https://www.fantacalcio.it' + link  # Aggiusta il link se è relativo
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Usa il timestamp corrente
            news.append({'source': 'Fantacalcio', 'title': title, 'link': link, 'timestamp': timestamp})

        return news

    except Exception as e:
        print(f"Errore nel recupero delle notizie da Fantacalcio: {e}")
        return []
    
def get_skysport_news():
    try:
        url = 'https://sport.sky.it/calcio/serie-a'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        news = []
        # Trova la sezione principale che contiene gli articoli
        articles = soup.find_all('a', class_='s-hero-clickable-area')

        for article in articles:
            title = article.find('article').find('h2').get_text(strip=True)
            link = article['href']
            # Verifica se il link è relativo e aggiungi il dominio, se necessario
            if not link.startswith('https'):
                link = 'https://sport.sky.it' + link
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Usa il timestamp corrente
            news.append({'source': 'SkySport', 'title': title, 'link': link, 'timestamp': timestamp})

        return news

    except Exception as e:
        print(f"Errore nel recupero delle notizie da SkySport: {e}")
        return []
    
def get_tuttomercatoweb_news():
    try:
        url = 'https://www.tuttomercatoweb.com/serie-a/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'lxml')

        news = []
        # Trova tutte le notizie presenti all'interno del div con classe 'tcc-list-news'
        articles = soup.find_all('a', href=True)

        for article in articles:
            # Filtra solo i link che puntano alle notizie di Serie A
            if '/serie-a/' in article['href']:
                title = article.get('title', None)  # Usa None come valore predefinito se non c'è titolo

                # Salta l'articolo se il titolo non è disponibile
                if not title or title == 'Titolo non disponibile':
                    continue

                link = article['href']
                # Verifica se il link è relativo e aggiungi il dominio, se necessario
                if not link.startswith('https'):
                    link = 'https://www.tuttomercatoweb.com' + link

                # Aggiungi la notizia all'elenco con il timestamp corrente
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                news.append({'source': 'TUTTOmercatoWEB', 'title': title, 'link': link, 'timestamp': timestamp})

        return news

    except Exception as e:
        print(f"Errore nel recupero delle notizie da TUTTOmercatoWEB: {e}")
        return []


def get_all_news():
    gazzetta_news = get_gazzetta_news()
    fantacalcio_news = get_fantacalcio_news()
    skysport_news = get_skysport_news()  
    tuttomercatoweb_news = get_tuttomercatoweb_news()
    all_news = gazzetta_news + fantacalcio_news + skysport_news + tuttomercatoweb_news
    return all_news
