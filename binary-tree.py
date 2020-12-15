class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self,value):
        if value < self.value: # If value is less than root value go left
            if self.left is None:  # If no left value than set it
                self.left = Node(value)  
            else:                       
                self.left.insert(value) # Repeat process until reached end of tree
        else:                       # If value is more than root value go right
            if self.right is None:   # If no right value than set it
                self.right = Node(value)  # Repeat process until reached end of tree
            else:
                self.right.insert(value)
    
    def in_order_search(self,value): # Search from left to right
        if value < self.value:  # If value is less than root value go left  
            if self.left is None: # If no more values, it was not found
                return f'{value} was not found'
            return self.left.in_order_search(value)   # Repeat process until either found or reached end of tree
        elif value == self.value:  # If value is found return it
                return f'{value} was found'
        else:                        # If value is more than root value go right
            if self.right is None:   # If no more values, it was not found
                return f'{value} was not found'
            return self.right.in_order_search(value)  # Repeat process until either found or reached end of tree
    
    def in_order_print(self):  
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    def pre_order_search(self,value): # Search by checking root, then left, then right
        if self.value == value:  # If value is found return it
            return f'{value} was found'
        elif value < self.value:  # If value is less than root value go left                
            if self.left is None:   # If no more values, it was not found
                return f'{value} was not found'
            return self.left.pre_order_search(value)  # Repeat process until either found or reached end of tree
        else:
            if self.right is None:  # If value is more than root value go right
                return f'{value} was not found'  # If no more values, it was not found
            return self.right.pre_order_search(value) # Repeat process until either found or reached end of tree
    
    def pre_order_print(self):
        print(self.value)
        if self.left:
            self.left.pre_order_print()
        if self.right:
            self.right.pre_order_print()

    def post_order_search(self,value):  # Search from left then right then root
        if value < self.value:         # If value is less than root value go left
            if self.left is None:      # If no more values, it was not found
                return f'{value} was not found'  
            return self.left.post_order_search(value)  # Repeat process until either found or reached end of tree
        elif value > self.value:       # If value is more than root value go right
            if self.right is None:      # If no more value, it was not fond
                return f'{value} was not found'
            return self.right.post_order_search(value)   # Repeat process until either found or reached end of tree
        else: 
            return f'{value} was found'
    
    def post_order_print(self):
        if self.left:
            self.left.post_order_print()
        if self.right:
            self.right.post_order_print()
        print(self.value)
    
    def invert(self):   # Invert a binary tree by switching the nodes
        if self.left:   # If left node exists go left until end of tree
            self.left.invert() 
        if self.right:  # If right node exists go right until end of tree
            self.right.invert()
        leftVal = self.left # Save left node value
        self.left = self.right # Set left node to right node value
        self.right = leftVal # Set the right node to saved left value

    def delete(self,value,parent=None):
        parentNode = parent
        
        if self.value == value:  # If value is found return it
            if self.left is None and self.right is None:
                if self.value < parentNode.value:
                    parentNode.left = None
                else:   
                    parentNode.right = None
            elif self.left is None:
                if self.value < parentNode.value:
                    parentNode.left = self.right
                else:
                    parentNode.right = self.right
            elif self.right is None:
                if self.value < parentNode.value:
                    parentNode.left = self.left
                else:
                    parentNode.right = self.left
            else:
                if self.value < parentNode.value:
                    parentNode.left = self.left
                    parentNode.left.right = self.right
                else:
                    parentNode.right = self.right
                    parentNode.right.left = self.left
            return f'{value} was deleted'   
        elif value < self.value:  # If value is less than root value go left                
            if self.left is None:   # If no more values, it was not found
                return f'{value} was not found'
            parentNode = self
            return self.left.delete(value,parentNode)  # Repeat process until either found or reached end of tree
        else:
            if self.right is None:  # If value is more than root value go right
                return f'{value} was not found'  # If no more values, it was not found
            parentNode = self
            return self.right.delete(value, parentNode) # Repeat process until either found or reached end of tree
    


root = Node(10)
root.insert(7)
root.insert(9)
root.insert(5)
root.insert(14)
root.insert(12)
root.insert(9)
root.in_order_print()
print('-----')
root.delete(9)
root.delete(5)
root.delete(14)
root.insert(5)
root.delete(7)
root.insert(11)
root.insert(13)
root.delete(12)
root.in_order_print()










