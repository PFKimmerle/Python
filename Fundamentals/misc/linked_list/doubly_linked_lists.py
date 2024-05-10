from DoublyLinkedList import DoublyLinkedList

if __name__ == "__main__":
    dll = DoublyLinkedList()
    # Add elements
    dll.add_to_end(10)
    dll.add_to_end(20)
    dll.add_to_end(30)
    
    # Print all elements
    print("Initial list:")
    dll.print_values()
    
    # Insert a new value
    dll.insert_between(25, 20)
    print("\nAfter inserting 25 after 20:")
    dll.print_values()
    
    # Delete an element
    dll.delete_node(20)
    print("\nAfter deleting 20:")
    dll.print_values()
