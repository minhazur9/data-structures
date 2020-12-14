class Node:                         
    def __init__(self, value=None):
        self.value = value   
        self.next = None    
        self.prev = None  
 
class DLinkedList:
    # Setting first node to None
    def __init__(self):
        self.head = None
    
    def insert(self,value):
        new_node = Node(value)
        new_node.next = self.head   # Previous head becomes the next node of the new one
        new_node.prev = None     # The new_node does not have a previous value
        if(self.head is not None):
            self.head.prev = new_node   # Sets the new node to the previous pointer for the head
        self.head = new_node     # New node becomes the new head
    
    def listAll(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
    
    def delete(self,value):
        node = self.head
        previous = None
        if (self.head.value == value):
            self.head = node.next
            return 'node deleted'
        while node is not None:
            if(node.value == value):  
                previous.next = node.next # Set previous node pointer to skip its next node
                if node.next is not None:
                    node.next.prev = previous  # Sets the prev pointer of the node after the deleted one to point towards the previous node
                node = previous # Set the current node to previous to remove references to deleted node
                return 'Node deleted'
            previous = node # updates previous node
            node = node.next # update current node
        return 'Node not found'
    
    def search(self,value):
        node = self.head
        while node is not None:
            if(node.value == value):
                return node
            node = node.next
        return "Node not found"
    
    def size(self):
        node = self.head
        size = 0
        while node is not None:
            size += 1
            node = node.next
        return size

        
        










    