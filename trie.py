class Trie:
    def __init__(self):
        self.child = {}
    
    def insert(self,word):
        current = self.child # Set root dictionary
        for letter in word:   # Loop through the dictionary
            if letter not in current: # If letter is not in the current dictionary branch it off
                current[letter] = {}  
            current = current[letter] # Move to new letter in dictionary
        current['#'] = 1 
    
    def printTrie(self):
        current = self.child
        print(current)
        
    def search(self,word):
        current = self.child
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return '#' in current