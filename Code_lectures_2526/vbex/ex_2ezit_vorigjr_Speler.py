#https://dodona.be/nl/activities/962940240/

class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        return isinstance(other, Player) and self.name == other.name
        # True als other ook een Player is en de naam gelijk is
        # Python roept automatisch jouw __eq__-methode op wanneer je == gebruikt.
    def __lt__(self, other):# Vergelijk op shirtnummer (lager nummer = "kleiner")
        if isinstance(other, Player):
            if self.number < other.number:
                return True
            else: return False

        else:
            return NotImplemented
    #gpt raadt dit aan:
    # def __lt__(self, other):
    #     if isinstance(other, Player):
    #         return self.number < other.number
    #     return NotImplemented


    def __str__(self):
        return f"{self.name} ({self.number})"

# Maak 3 spelers en steek ze in een lijst
#
# Print één van de objecten
#
# Test de __eq__-methode
#
# Test de __lt__-methode door sorted toe te passen op de lijst
#
# Print de gesorteerde lijst
def main():
    player1 = Player("Eden Hazard", 10)
    player2 = Player("Moussa Dembele", 19)
    player3 = Player("Jan Vertonghen", 5)
    players = [player1, player2, player3]
    print(player1)
    print(player1.__eq__(player2)) # player1 == player2 is 100% hetzelfde als: p1.__eq__(p2)
    # same_name_diff_number = Player("Eden Hazard", 99)
    # print("p1 == same_name_diff_number?:", p1 == same_name_diff_number)  # True
    # print("p1 == p2?:", p1 == p2)

    #sorted(players) gebruikt jouw lt omdat:
    # Python moet elementen kunnen vergelijken
    # < op objecten → roept automatisch __lt__ op
    # jouw lt beslist welke speler “kleiner” is
    # dus bepaalt het de sorteervolgorde
    #WANT Maar objecten (zoals Player) kan Python niet vanzelf vergelijken,
    #python kent enkel < tss integers, floats, strings
    print("\nOngeordende lijst:")
    for p in players:
       print(p)
    sorted_players = sorted(players)
    print("\nGesorteerde lijst (op nummer):")
    for p in sorted_players:
        print(p)

if __name__ == "__main__":
    main()