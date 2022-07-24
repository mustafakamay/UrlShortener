import string
from random import choices
import os
from .models import UrlShortener

def generate_short_url():
    characters_in_short_url = string.ascii_letters + string.digits
    short_url = ''.join(choices(characters_in_short_url, k=5))

    unique_control = UrlShortener.objects.filter(shortUrl = short_url ).first()
    if unique_control:
        return generate_short_url()

    return short_url