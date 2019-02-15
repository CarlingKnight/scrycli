class Card:
    def __init__(self, result):
        card_attributes = ["name", "mana_cost", "eur", "type_line", "oracle_text", "cmc"]

        for key in card_attributes:
            try:
                setattr(self, key, result[key])
            except KeyError:
                setattr(self, key, "")

    def print(self):
        print("{} - {} - eur({})\n{}\n{}\n".format(self.name, self.mana_cost, self.eur, self.type_line, self.oracle_text))
