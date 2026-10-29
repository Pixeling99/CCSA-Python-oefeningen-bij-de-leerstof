class HashSet:
    


    def __init__(self, max_size=10):
        self.data = [None] * max_size
        self.deleted = [False] * max_size
        self.max_size = max_size
        self.number_items = 0
        
    def add(self, item):
        # toevoegen kan niet wanneer:
        # - Set zit vol
        # - Toe te voegen item zit al in de set (index_of geeft iets anders dan -1) -> -1 returnen (kan niet toevoegen)
        
        # Indien toevoegen wel kan
        # - number_items verhogen
        # - index van toevoegen zoeken -> initële index berkenen, indien bezet -> eerste vrije positie zoeken
        # - item in data plaatsen
        # - deleted op false zetten indien die op true was
        
        
        pass

    def index_of(self, item):
    
    index = hash(item) % self.max_size
    
    teller = 0
    while (self.data[index] is not None or self.deleted[index]) and self.data[index] != item and teller < self.max_size:
        index += 1
        teller += 1
        if index == self.max_size:
            index = 0
    
    return index if self.data[index] == item else -1

    def delete(self, item):
        # index item zoeken
        # indien -1 -> niets doen
        # indien niet -1 -> item staat op gevonden index -> data verwijderen dus op None zetten en deleted [index] op true zetten
        index = self.index_of(item)
        if index == -1:
            return False
        
        self.data[index] = None
        self.deleted[index] = True
        self.number_items -= 1
        return True
    
if __name__ == "__main__":
    hash_set = HashSet(max_size = 10)
    # TODO: operaties uitproberen


    





