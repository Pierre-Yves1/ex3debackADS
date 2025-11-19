import csv

class Node:
    """Node in de linked list: stelt één taak voor."""

    def __init__(self, task_name, duration, priority):
        self.task_name = task_name      # naam van de taak
        self.duration = duration        # duur in minuten
        self.priority = priority        # 1 = hoogste prioriteit
        self.next = None                # verwijzing naar de volgende node


class TaskLinkedList:
    """Linked list die taken ordent in de juiste volgorde."""

    def __init__(self):
        self.head = None
        self.tail = None

    # ----------------------------------------
    # Basisoperaties
    # ----------------------------------------

    def add_task(self, task_name, duration, priority):
        """Voeg een taak toe aan het einde van de lijst."""
        new_node = Node(task_name, duration, priority)

        if self.head is None:           # lijst is leeg
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node   # hang node achter de tail
            self.tail = new_node        # update tail

    def remove_task(self, task_name):
        """Verwijdert de eerste taak met deze naam."""
        current = self.head
        prev = None

        while current is not None:
            if current.task_name == task_name:

                # verwijderen van head
                if prev is None:
                    self.head = current.next
                    if current == self.tail:
                        self.tail = None

                # verwijderen in het midden/einde
                else:
                    prev.next = current.next
                    if current == self.tail:
                        self.tail = prev

                return True

            prev = current
            current = current.next

        return False  # niet gevonden

    def display_tasks(self):
        """Print alle taken in volgorde."""
        current = self.head
        while current is not None:
            print(
                f"Task: {current.task_name}, "
                f"duration={current.duration}, "
                f"priority={current.priority}"
            )
            current = current.next

    def find_task(self, task_name):
        """Zoek een taak op naam."""
        current = self.head
        while current is not None:
            if current.task_name == task_name:
                return current
            current = current.next
        return None

    def calculate_total_duration(self):
        """Som van alle durations."""
        total = 0
        current = self.head
        while current is not None:
            total += current.duration
            current = current.next
        return total

    # ----------------------------------------
    # CSV inlezen
    # ----------------------------------------

    def read_tasks_from_csv(self, file_path):
        """Lees taken in uit CSV: task_name,duration,priority."""
        with open(file_path, mode="r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                name = row[0]
                duration = int(row[1])
                priority = int(row[2])
                self.add_task(name, duration, priority)

    # ----------------------------------------
    # Helpermethodes voor sorteren
    # ----------------------------------------

    def sorted_insert_by_priority(self, head, node):
        """
        Voeg node in een nieuwe lijst toe, gesorteerd op priority.
        Kleinste priority eerst.
        """
        node.next = None  # ontkoppel node van oude lijst

        if head is None or node.priority < head.priority:
            node.next = head
            return node

        current = head
        while current.next is not None and current.next.priority <= node.priority:
            current = current.next

        node.next = current.next
        current.next = node
        return head

    def sorted_insert_by_priority_duration(self, head, node):
        """
        Voeg node toe gesorteerd eerst op priority,
        dan op duration (kortste taak eerst).
        """
        node.next = None

        def comes_before(a, b):
            if a.priority < b.priority:
                return True
            if a.priority > b.priority:
                return False
            return a.duration < b.duration  # zelfde priority → kortste eerst

        if head is None or comes_before(node, head):
            node.next = head
            return node

        current = head
        while current.next is not None and not comes_before(node, current.next):
            current = current.next

        node.next = current.next
        current.next = node
        return head

    # ----------------------------------------
    # Reorder-methodes
    # ----------------------------------------

    def reorder_tasks_by_priority(self):
        """Herorden oplopend op priority."""
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            new_head = self.sorted_insert_by_priority(new_head, current)
            current = next_node

        self.head = new_head
        self.update_tail()

    def reorder_tasks_by_priority_duration(self):
        """Herorden op priority, dan duration."""
        new_head = None
        current = self.head

        while current is not None:
            next_node = current.next
            new_head = self.sorted_insert_by_priority_duration(new_head, current)
            current = next_node

        self.head = new_head
        self.update_tail()

    def update_tail(self):
        """Tail opnieuw bepalen na herordening."""
        self.tail = None
        current = self.head
        while current is not None:
            if current.next is None:
                self.tail = current
            current = current.next


# ----------------------------------------
# Example / demo (optioneel)
# ----------------------------------------

def main():
    tasks = TaskLinkedList()

    tasks.read_tasks_from_csv("tasks.csv")

    print("=== Original tasks ===")
    tasks.display_tasks()
    print()

    tasks.reorder_tasks_by_priority()
    print("=== After priority reorder ===")
    tasks.display_tasks()
    print()

    tasks.reorder_tasks_by_priority_duration()
    print("=== After priority + duration reorder ===")
    tasks.display_tasks()
    print()


if __name__ == "__main__":
    main()
