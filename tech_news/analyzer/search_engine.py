from datetime import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = {"title": {"$regex": title, "$options": "i"}}
    return [(_["title"], _["url"]) for _ in search_news(query)]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""
    try:
        iso_date = datetime.fromisoformat(date)
        query = {"timestamp": {"$regex": iso_date.strftime("%d/%m/%Y")}}
        return [(_["title"], _["url"]) for _ in search_news(query)]
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    query = {"tags": {"$regex": tag, "$options": "i"}}
    return [(_["title"], _["url"]) for _ in search_news(query)]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = {"category": {"$regex": category, "$options": "i"}}
    return [(_["title"], _["url"]) for _ in search_news(query)]
