import dateparser
from dateparser.search import search_dates
from datetime import datetime

def parse_datetime(text: str):
    settings = {
        "PREFER_DATES_FROM": "future",
        "RELATIVE_BASE": datetime.now(),
    }

    result = search_dates(text, settings=settings)

    if result:
        return result[0][1]

    return None
