import csv  #staat hier voor de functie read_tasks_from_cvc rond line 68
class Node:
    def __init__(self, task_name, duration, priority): #ne constructor die werkt met zijn element e
        self.task_name = task_name
        self.duration = duration
        self.priority = priority
        self.next = None

class LinkedList:
    def __init__(self):
        self.__head = None # __ betekent: Het betekent dat de variabele privé is voor de klasse., je kan ze niet van buiten de klasse aanpassen
        self.__tail = None
        self.__size = 0

    def add_task(self, task_name, duration, priority):
        newtask = Node(task_name, duration, priority)
        if self.__tail is None:
            self.__head = self.__tail = newtask
        else:
            self.__tail.next = newtask
            self.__tail = newtask

        self.__size += 1

    def remove_task(self, task_name):
        current = self.__head
        prev = None
        while current is not None:
            if current.task_name == task_name:
                if prev is None:
                    self.__head = current.next

                    if current == self.__tail:
                        self.__tail = None

                else:
                    prev.next = current.next

                    if current == self.__tail:
                        self.__trail = prev

                self.__size -= 1
                return True
            prev = current
            current = current.next

        return False

    def display_tasks(self):
        # if self.__head is None:        # of: if self.__size == 0:
        #     print("Geen taken in de lijst.")
        #     return
        current = self.__head
        while current is not None:
            print(current.task_name, current.duration, current.priority)
            current = current.next

    def find_task(self, task_name):
        current = self.__head
        while current is not None:
            if current.task_name == task_name:
                return current
            current = current.next
        return None

    def calculate_total_duration(self):
        current = self.__head
        duration = 0
        while current is not None:
            duration += current.duration
            current = current.next
        return duration

    def read_tasks_from_cvc(self, file_path): #ook andere manier zie opl.py, of hieronder in ##
        try:
            file = open(file_path, "r")
            lines = file.readlines()
            #met DictReader zie word smv
            file.close()
            if len(lines) <= 1: #als = 1 heeft het bestand enkel een header: task_name, dur, prior en dus geen echte waarden
                print("Leeg CSV-bestand.")
                return

            for line in lines[1: ]:#eerste lijn is header en boeit niet
                line = line.strip()
                if line =="":
                    continue #skip lege rijen

                parts = line.split(",") #split op komma
                name = parts[0]
                duration = int(parts[1])
                priority = int(parts[2])
                self.add_task(name, duration, priority)

            print(f"Tasks geladen uit {file_path}")

        except FileNotFoundError:
            print(f"Bestand niet gevonden: {file_path}")


        #DIT IS ALS JE MET WITH OPEN WILT WERKEN
        # try:
        #     with open(file_path, mode='r') as file:
        #         reader = csv.DictReader(file)  # leest kolomnamen automatisch
        #
        #         for row in reader:
        #             name = row["task_name"]
        #             duration = int(row["duration"])
        #             priority = int(row["priority"])
        #
        #             self.add_task(name, duration, priority)
        #
        #     print(f"Tasks geladen uit {file_path}")
        #
        # except FileNotFoundError:
        #     print(f"Bestand niet gevonden: {file_path}")


    ## write_tasks_to_csv() (het omgekeerde): NIET GEVR IN DEZE OPDRACHT
    # def write_tasks_to_csv(self, file_path):
    #     """Schrijft alle tasks uit de linked list naar een CSV-bestand."""
    #     # Bestand openen in schrijfmodus ("w" = overschrijven)
    #     file = open(file_path, "w")
    #
    #     # Header schrijven
    #     file.write("task_name,duration,priority\n")
    #
    #     # Alle nodes overlopen en elke task als lijn in CSV schrijven
    #     current = self.__head
    #     while current is not None:
    #         line = f"{current.task_name},{current.duration},{current.priority}\n"
    #         file.write(line)
    #         current = current.next
    #
    #     # Bestand sluiten
    #     file.close()
    #     print(f"Tasks weggeschreven naar {file_path}")

    def sorted_insert_by_priority(self, head, node):#head, met andere woorden: het begin van een linked list, het is gewoon de eerste node van een (tijdelijke) linked list
        #head = eerste node van de nieuwe tijdelijke lijst die je opbouwt die al gesorteerd is
        # node = de node die je wilt invoegen
        # Je maakt dus geen nieuwe LinkedList-class, maar gewoon een pointer naar de eerste node van een nieuwe gesorteerde lijst.
        #Lower priority number = higher priority: nodes met laagste priority komen eerst
        if head is None: # Case 1: lege lijst → node wordt eerste element
            node.next = None
            return node

        if node.priority < head.priority: # Case 2: node moet VOOR de huidige head komen, priority node kleiner dan die van head
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.priority <= node.priority: #Zolang de volgende node (current.next)
            # een priority heeft die kleiner of gelijk is aan de priority van de nieuwe node, mag node nog niet ingevoegd worden –
            # want dan zou node vóór iemand komen met hogere prioriteit (lager nummer).
            #!!!!!!# vb zo: head → [P=1] → [P=3] → [P=4] → [P=5] → None
            current = current.next # Dus we schuiven door:

            #Wanneer stopt de while?

            # Hij stopt in 2 gevallen:
            #
            # Einde lijst:
            # current.next is None
            # → we zitten aan de laatste node, node moet helemaal achteraan.
            #
            # We vinden een grotere priority:
            # current.next.priority > node.priority
            # → de volgende node heeft een slechtere prioriteit (hoger getal) dan node,
            # → node moet tussen current en current.next komen.
            # Na de while staan we dus op de juiste current.

        # Node invoegen
        node.next = current.next
        current.next = node
        return head
         # Wat geven we terug?
           # Altijd: de eerste node van de (nieuwe) lijst.

    # onderstaand: HELPER 2: sorted_insert_by_priority_duration
    # Voegt één node in in een (al gesorteerde) linked list
    # op basis van:
    #   1) priority (lager getal = belangrijker)
    #   2) bij gelijke priority: duration (korter eerst)
    #
    # head: begin van de NIEUWE (gesorteerde) lijst
    # node: node die ingevoegd wordt
    #
    # Geeft de (mogelijk nieuwe) head van de lijst terug.
    def sorted_insert_by_priority_duration(self, head, node):
        if head is None: #lege lijst
            node.next = None
            return node

        # Node komt vóór head?
        if (node.priority < head.priority) or \
            (node.priority == head.priority and node.duration < head.duration):
            node.next = head
            return node


        # Zoek juiste plek verder in de lijst # Anders zoeken we de juiste plek verder in de lijst
        current = head
        while current.next is not None:
            # node hoort vóór current.next als hij "beter" is:
            if (node.priority < current.next.priority) or \
                    (node.priority == current.next.priority and node.duration < current.next.duration):
                break  # als het zo is stoppen we de while loop

            current = current.next  # als het niet zo is verschuiven we

        node.next = current.next #node invoegen na current # stel A, B en we voegen C ertussen in
                        #de current next van A is momenteel B, maar C komt ertussen, de next van C zal dus B zijn
        current.next = node
        return head



    # REORDER 1: reorder_tasks_by_priority
    #        Maakt een nieuwe gesorteerde lijst op basis van priority alleen.
           #Laagste priority-nummer komt eerst.
    # Na afloop verwijst self.head naar de gesorteerde lijst.

    def reorder_tasks_by_priority(self):
        new_head = None #new_head is nieuwe gesorteerde lijst in opbouw, nieuwe lege lijst
        current = self.__head #die self__head is de oude lijst die we doorlopen, current is eerste node, dus head v die list

        while current is not None:
            next_node = current.next # oude link bewaren
            current.next = None # We knippen current los van de oude lijst Omdat we current gaan invoegen in de nieuwe gesorteerde lijst
            new_head = self.sorted_insert_by_priority(new_head, current) # we stoppen current in de nieuwe gesorteerde lijst
            current = next_node

        # nieuwe head instellen
        self.__head = new_head # self.__head wordt het begin van de NIEUWE lijst


        # tail opnieuw uitrekenen: We lopen door de nieuwe lijst tot we de laatste node vinden:
        if new_head is None:
            self.__tail = None
        else:
            tail = new_head
            while tail.next is not None:
                tail = tail.next
            self.__tail = tail
        # size blijft hetzelfde, dus __size hoeft niet aangepast


    #  Maakt een nieuwe gesorteerde lijst:
    #         1) eerst op priority (laagste eerst)
    #         2) dan op duration (kortste eerst)
    def reorder_tasks_by_priority_duration(self):
        new_head = None
        current = self.__head
        while current is not None:
            next_node = current.next # oude link bewaren
            current.next = None #  node losmaken uit oude
            new_head = self.sorted_insert_by_priority_duration(new_head, current) #invoegen in nieuwe
            current = next_node

        self.__head = new_head
        if new_head is None:
            self.__tail = None

        else:
            tail = new_head
            while tail.next is not None:
                tail = tail.next
            self.__tail = tail






