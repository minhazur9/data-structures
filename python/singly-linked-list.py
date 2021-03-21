
class Node:                         
    def __init__(self, value=None):
        self.value = value   
        self.next = None      
 
class SLinkedList:
    # Setting first node to None
    def __init__(self):
        self.head = None
    
    # To add a new node
    def insert(self,value):
        new_node = Node(value)  
        new_node.next = self.head   # Previous head becomes the next node of the new one
        self.head = new_node     # New node becomes the new head
    
    # List all Nodes
    def listAll(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next
    
    def delete(self,value):
        node = self.head
        previous = None
        if(node.value == value):
            self.head = node.next 
            return 'Node deleted'
        while node is not None:
            if(node.value == value):  
                previous.next = node.next  # Set previous node pointer to skip and link to node after deleted one
                node = previous  # update current node
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
    
    def reverse(self):
        previous = None
        node = self.head
        while node is not None:
            nextNode = node.next  # Saving the next node
            node.next = previous  # Setting pointer to link to the previous node
            previous = node # updating previous node
            node = nextNode # updating current node
        self.head = previous # Setting head to last node