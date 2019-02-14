from urllib.parse import urlencode
import requests
import json


def print_query(query):
    payload = urlencode({'q': query})
    print("Sending payload {}".format(payload))
    response = requests.get("https://api.scryfall.com/cards/search", params=payload)

    if response.status_code == 404:
        print("Your search sucked, nothing showed up.")
        return

    cards = json.loads(response.text)['data']
    for card in cards:
        if "card_faces" in card:
            print("{} is a multi-sided card, we don't quite support those yet.".format(card["name"]))
            return
        else:
            output_text = "{} - {}\n" \
                          "{}\n".format(card["name"], card["mana_cost"], card["oracle_text"])
            print(output_text)
