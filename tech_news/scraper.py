from parsel import Selector

from time import sleep

from requests import HTTPError, ReadTimeout, get

from tech_news.database import create_news

# Requisito 1


def fetch(url):
    """Seu código deve vir aqui"""
    try:
        sleep(1)
        response = get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (ReadTimeout, HTTPError):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    return selector.css("h2.entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    return selector.css("a.next::attr(href)").get()


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get().strip()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = len(selector.css("h5.reply-title::text").getall()) or 0
    summary = selector.xpath("string(//p)").get().strip()
    tags = selector.css("section.post-tags li a::text").getall()
    category = selector.css("span.label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    URL = "https://blog.betrybe.com/"

    news = list()
    news_info = list()
    next_page = "/"

    while len(news) < amount and next_page:
        fetch_html = fetch(URL)
        news.extend(scrape_updates(fetch_html))
        URL = scrape_next_page_link(fetch_html)
        next_page = Selector(fetch_html).css("a.next ::attr(href)").get()

    for _ in news[:amount]:
        content = fetch(_)
        news_info.append(scrape_news(content))

    create_news(news_info)
    return news_info
