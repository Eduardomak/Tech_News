# Requisito 10
from collections import Counter
from operator import itemgetter

from tech_news.database import find_news


def top_5_news():
    """Seu código deve vir aqui"""
    primary_key_sort = sorted(
        find_news(),
        key=itemgetter("comments_count"),
        reverse=True,
    )[:5]
    return [(_["title"], _["url"]) for _ in primary_key_sort]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    categories = Counter(_["category"] for _ in find_news()).most_common(5)
    secondary_key_sort = sorted(
        categories,
        key=itemgetter(0),
    )
    primary_key_sort = sorted(
        secondary_key_sort,
        key=itemgetter(1),
        reverse=True,
    )
    return [_[0] for _ in primary_key_sort]
