# scraper.py
import aiohttp
from bs4 import BeautifulSoup


async def scrape_news(url: str, use_proxy: bool, proxy_host: str, proxy_port: int) -> list:

    news_items = []
    proxy_url = f"http://{proxy_host}:{proxy_port}" if use_proxy else None


    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, proxy=proxy_url) as response:
                response.raise_for_status() 
                html_content = await response.text()

        soup = BeautifulSoup(html_content, 'html.parser')



        for headline in soup.find_all('article'):
            title_tag = headline.find(['h2', 'h3', 'a'], class_=['title', 'media__title', 'item-title'])
            link_tag = headline.find('a')

            title = title_tag.get_text(strip=True) if title_tag else "Judul Tidak Ditemukan"
            link = link_tag['href'] if link_tag and 'href' in link_tag.attrs else "Link Tidak Ditemukan"


            if title != "Judul Tidak Ditemukan" and link != "Link Tidak Ditemukan" and link.startswith('http'):
                news_items.append({'title': title, 'link': link})

        return news_items[:5]
    except aiohttp.ClientError as e:
        print(f"Aiohttp error during scraping: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred during scraping: {e}")
        return []
