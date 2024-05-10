class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        new_node = SLNode(val)
        if self.head is None:
            self.head = new_node
            return self
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    # BONUS: Method to remove from the front
    def remove_from_front(self):
        if self.head is None:
            return None
        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    # BONUS: Method to remove from the back
    def remove_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            removed_value = self.head.value
            self.head = None
            return removed_value
        runner = self.head
        while runner.next.next:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    # BONUS: Method to remove a node by value
    def remove_val(self, val):
        if self.head is None:
            return None
        if self.head.value == val:
            return self.remove_from_front()
        runner = self.head
        while runner.next:
            if runner.next.value == val:
                removed_value = runner.next.value
                runner.next = runner.next.next
                return removed_value
            runner = runner.next
        return None

    # BONUS: Method to insert a node at a specific index
    def insert_at(self, val, n):
        if n == 0:
            self.add_to_front(val)
            return self
        new_node = SLNode(val)
        runner = self.head
        index = 0
        while index < n - 1:
            if runner is None:
                return self  # Out of bounds
            runner = runner.next
            index += 1
        new_node.next = runner.next
        runner.next = new_node
        return self

# Testing the SList class
my_list = SList()
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values()
# Should output:
# Linked lists
# are
# fun!
