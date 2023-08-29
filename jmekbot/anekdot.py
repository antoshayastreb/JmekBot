import aiohttp
from bs4 import BeautifulSoup

stop_filters = [
    'читать дальше'
]

class AnekdotRuScraper:

    @staticmethod
    async def fetch_page():
        url = 'https://www.anekdot.ru/'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
            
    @staticmethod
    async def get_anekdots():
        html = await AnekdotRuScraper.fetch_page()
        soup = BeautifulSoup(html, 'html.parser')

        anekdots = []
        
        for div in soup.find_all('div', {'class': 'topicbox'}):
            # Пропустим блоки с картинками
            if div.find('img') is not None:
                continue
            
            main_text = div.find_all('div', {'class': 'text'})

            if main_text:
                text = main_text[0].get_text().strip()

            if text:

                if any(stop_item in text for stop_item in stop_filters):
                    continue

                anekdots.append(text)

        return anekdots