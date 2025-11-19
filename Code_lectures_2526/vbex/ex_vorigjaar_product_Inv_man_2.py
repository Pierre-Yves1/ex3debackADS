from ex_vorigjaar_product_Inv_man import Product, Batch
import random #ik vind ook op internet: from random import randint

class Inventory_Manager:
    def __init__(self):
        self.products = {} #dictionary


        #Voegt een nieuw product toe aan de voorraad.
        #Als het product al bestaat → foutmelding printen.
    def add_product(self, product_name, holding_cost, stockout_penalty):
        if product_name in self.products:
            print(f"Product {product_name} already exists.")
        else:
            self.products[product_name] = Product(product_name, holding_cost, stockout_penalty)

        #Voegt een nieuwe batch toe aan een product-stack.
    def restock_product(self, product_name, quantity, cost_per_unit):
        if product_name not in self.products:
            print(f"Product {product_name} not found")
            return #return want als niet in dict, dan moet je deze ftie stoppen
                    #zodat alles eronder niet meer uitgevoerd wordt

        self.products[product_name].add_batch(quantity, cost_per_unit)

    def simulate_demand(self, min_deman = 0, max_demand = 20):
        # Genereert een willekeurige vraag voor elk product (1 punt). De methode retourneert
        # een woordenboek waarbij de sleutel product_name is en de waarde de vraag is die overeenkomt
        # met een willekeurige waarde tussen min_demand en max_demand. Standaard is min_demand gelijk
        # aan 0 en max_demand gelijk aan 20
        demands = {}
        for name in self.products:
            amount = random.randint(min_deman, max_demand)
            demands[name] = amount
        return demands


    #Simuleert een dag van operaties en retourneert de totale aanhoudingskosten
    # en totale stockout-kosten (2 punten). De parameter van de methode komt overeen met
    # de gesimuleerde vraag als een woordenboek (zie methode simulate_demand).
    def simulate_day(self, demand):
        total_holding_cost = 0
        total_stockout_cost = 0

        # name en product zijn gewoon nieuwe variabelen die je zelf maakt binnen de for-loop.
        # Ze verwijzen naar de key en de value van de dictionary self.products.
        # key = "Widget"
        # value = Product-object dat hoort bij “Widget”
        # → self.products.items() geeft paren (key, value) terug.
        for name, product in self.products.items():
            product_demand = demand.get(name, 0) # “Geef mij de waarde voor key name in de dictionary demand,en als die key NIET bestaat, geef dan 0 terug.
            stockout_cost = product.fulfill_demand(product_demand)
            holding_cost = product.calculate_holding_cost()
            total_stockout_cost += stockout_cost
            total_holding_cost += holding_cost

        return total_holding_cost, total_stockout_cost

    def save_to_csv(self, filename):
        # Bestand openen in schrijfmodus ("w" = overschrijven)
        file = open(filename, "w")

        # # Header schrijven
        file.write("product_name, batch_quantity, batch_cost_per_unit\n")
        for name, product in self.products.items():
            for batch in product.batches:
                line = f"{name}, {batch.quantity}, {batch.cost_per_unit}\n"
                file.write(line)
        file.close()


    #  Laadt voorraad uit CSV.
    #         Als een product nog niet bestaat, wordt het aangemaakt
    #         met holding_cost = 0 en stockout_penalty = 0 (want deze info staat niet in het CSV).

    def load_from_csv(self, filename):
        try:
            file = open(filename, "r")
        except FileNotFoundError:
            print(f"File {filename} not found")
            return

        lines = file.readlines()
        file.close()

        if len(lines) <= 1:
            print("Empty CSV")
            return

        for line in lines[1:]:  # header overslaan
            line = line.strip()
            if line == "":
                continue

            parts = line.split(",")
            name = parts[0]
            quantity = int(parts[1])
            cost = float(parts[2])

            if name not in self.products:
                self.products[name] = Product(name, 0, 0)

            self.products[name].add_batch(quantity, cost)

    def print_inventory(self):
        #Print de voorraad voor elk product, zoals in het voorbeeld.
        print("Current Inventory:")
        for product in self.products.values():
            print(product)
            print()  # lege lijn tussen producten

def main():

    manager = Inventory_Manager()
    # Voeg 2 producten toe
    manager.add_product("Widget", 0.2,2.5)
    manager.add_product("Gadget", 0.3,3.0   )
    # Vul elk product met minstens 2 batches
    manager.restock_product("Widget", 10, 2.5)
    manager.restock_product("Widget", 5, 2.8)

    manager.restock_product("Gadget", 7, 3.0)
    manager.restock_product("Gadget", 8, 3.1)

    # Print huidige voorraad
    manager.print_inventory()

    # Simuleer vraag
    demand = manager.simulate_demand()
    print("Demand:", demand)

    total_holding, total_stockout = manager.simulate_day(demand)
    print("Total holding cost:", total_holding)
    print("Total stockout cost:", total_stockout)

    # Sla op in CSV
    manager.save_to_csv("inventory.csv")

#Deze regel zorgt ervoor dat main() alleen wordt uitgevoerd wanneer je het bestand runt,
# maar niet wanneer het bestand geïmporteerd wordt door een ander bestand.
if __name__ == "__main__":
    main()


