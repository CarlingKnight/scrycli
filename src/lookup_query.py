from urllib.parse import urlencode
from src.card import Card
import operator
import requests
import json


def print_query(query, sort_by="cmc"):
    payload = urlencode({'q': query})
    print("Sending payload {}".format(payload))
    response = requests.get("https://api.scryfall.com/cards/search", params=payload)
    cards = []

    if response.status_code == 404:
        print("Your search sucked, nothing showed up.")
        return

    results =  json.loads(response.text)['data']
    for result in results:
        if "card_faces" in result:
            print("{} is a multi-sided card, we don't quite support those yet.".format(result["name"]))
            continue
        else:
            cards.append(Card(result))

    sorted_cards = sorted(cards, key=operator.attrgetter(sort_by))

    for card in sorted_cards:
        card.print()
