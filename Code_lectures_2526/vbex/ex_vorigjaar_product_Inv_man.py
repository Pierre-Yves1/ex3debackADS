
class Batch:
    def __init__(self, quantity, cost_per_unit):
        self.quantity = quantity # hoeveelheid van het product in deze batch
        self.cost_per_unit = cost_per_unit  # kost per eenheid in deze batch

    def __str__(self): #dit is de tostring-methode str die de batch weergeeft
        return f"Batch(quantity={self.quantity}, cost_per_unit={self.cost_per_unit})"
                 #"Hoe moet dit object eruitzien wanneer je het print?"
                #als ik print(batch) doe, dan roept Python automatisch dit op: batch.__str__()

class Product:
    def __init__(self, product_name, holding_cost, stockout_penalty):
        self.product_name = product_name
        #!!!!!!!!! we gebruiken een Python-lijst als stack (top = laatste element)
        self.batches = [] #!!!!!!!!!#'stack van batches voor het product'
        # kost om 1 eenheid op voorraad te houden
        self.holding_cost = holding_cost
        # kost per niet-geleverde eenheid
        self.stockout_penalty = stockout_penalty

    def add_batch(self, quantity, cost_per_unit): # Voeg een batch toe bovenop de stack
        self.batches.append(Batch(quantity, cost_per_unit))
        # OF:
        # batch = Batch(quantity, cost_per_unit)
        # #LIFO: laatst toegevoegde batch ligt bovenaan
        # self.batches.append(batch)

    # 2) Vervul vraag (LIFO, via bovenste batch)
    #Vervult de vraag met behulp van de bovenste batch van de voorraad.
    # -Als de totale voorraad de vraag dekt → return 0
    # -Als de vraag niet volledig kan worden ingevuld:
    #  return stockout_penalty * aantal_niet_geleverde_eenheden
    def fulfill_demand(self, demand):
        remaining = demand
        # Terwijl er nog vraag is en er batches zijn
        while remaining > 0 and self.batches:
            top_batch = self.batches[-1] # bovenste batch (LIFO)

            if top_batch.quantity > remaining:
                # Bovenste batch heeft genoeg om de resterende vraag te dekken
                top_batch.quantity -= remaining
                remaining -= 0
            else:
                # Bovenste batch is niet genoeg → volledig opgebruiken en verwijderen
                remaining -= top_batch.quantity
                self.batches.pop()

        # Als alles geleverd is
        if remaining == 0:
            return 0

        # Niet alles kon geleverd worden → stockout penalty
        return remaining * self.stockout_penalty

    #Totale aanhoudingskosten: holding_cost * (totaal aantal eenheden in alle batches)
    def calculate_holding_cost(self):
        total_quantity = sum(batch.quantity for batch in self.batches)
        return total_quantity * self.holding_cost

    def __str__(self):
        # Vorm zoals in de opgave:
        # Product [product_name]:
        #     Batch(quantity=[...], cost_per_unit=[...])
        #     Batch(quantity=[...], cost_per_unit=[...])
        #     ...
        lines = [f"Product {self.product_name}:"]
        if not self.batches:
            lines.append("  (geen batches in voorraad)")
        else:
            for batch in self.batches:
                lines.append(str(batch)) #deze verwijst naar de __str__ in de vorige class Batch zie bovenaan

        return "\n".join(lines)
        #Neem alle strings in de lijst lines en plak ze aan elkaar met een nieuwe lijn ertussen."
        #dit doet dus de 2 uiterste haakjes symbolen vd lijst weg en verandert de komma's die tss de elementen
        #vd lijst staan naar spaties

        #  " ".join(list) plakt dingen samen met spaties
        #  ",".join(list) plakt dingen samen met komma’s
        #  "\n".join(list) plakt dingen samen met nieuwe lijnen → ideaal voor text blocks

    # -------------------------
    # Klein testje (optioneel)
    # -------------------------
    # if __name__ == "__main__":
    #     p = Product("Laptop", holding_cost=0.5, stockout_penalty=10)
    #
    #     p.add_batch(10, 800)
    #     p.add_batch(5, 820)  # deze komt bovenop de stack (LIFO)
    #
    #     print(p)
    #     print("Holding cost:", p.calculate_holding_cost())
    #
    #     penalty = p.fulfill_demand(12)
    #     print("\nNa vraag van 12 stuks:")
    #     print(p)
    #     print("Penalty:", penalty)
    #     print("Nieuwe holding cost:", p.calculate_holding_cost())
    #
