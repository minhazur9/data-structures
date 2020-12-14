
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
            self.head = node.next # Set head as next node if first value deleted
            return 'Node deleted'
        while node is not None:
            if(node.value == value):  
                previous.next = node.next # Set previous node pointer to skip its next node
                node = previous # Set the current node to previous to remove references to deleted node
                return 'Node deleted'
            previous = node # updates previous node
            node = node.next # update current node
        return 'Node not found'
    
    def search(self,value):
        node = self.head
        while node is not None:
            if(node.value == value):
                return node.value
            node = node.next
        return "Node not found"
    
    def size(self):
        node = self.head
        size = 0
        while node is not None:
            size += 1
            node = node.next
        return size




list1 = SLinkedList()
list1.insert("Mon")
list1.insert("Tues")
list1.insert("Wed")
list1.insert("Thurs")
list1.insert("Fri")
list1.listAll()
print(list1.size())
