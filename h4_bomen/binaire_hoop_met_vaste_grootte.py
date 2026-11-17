class BinaryHeap:

    def __init__(self, max_size=10):
        self._num_elements = 0
        self._data = [None] * max_size

    def is_empty(self):
        return self._num_elements == 0
    
    def get_min_elem(self):
        if self.is_empty():
            raise ValueError("get min elements on empty heap")
        return self._data[0]

    def insert_elem(self, item):
        if self._num_elements == len(self._data):
            raise ValueError("Insert on full heap")
        index = self._num_elements
        self._num_elements += 1
        self._data[index] = item
        
        while index != 0 and item < self._data[self._parent(index)]:        
            self._swap(index, self._parent(index))
            index = self._parent(index)

    def remove_min_elem(self):
        min_element = self.get_min_elem()
        self._num_elements -= 1
        self._data[0] = self._data[self._num_elements]
        self._data[self._num_elements] = None
        
        index = 0
        elem = self._data[index]
        
        while not self._is_leaf(index) and  elem > self._data[self._index_min_child(index)]:
            child_index = self._index_min_child(index)
            self._swap(index, child_index)
            index = child_index
        return min_element
    def _swap(self, i1, i2):
        self._data[i1], self._data[i2] = self._data[i1], self._data[i2]
    
    @staticmethod
    def _parent(index):
        
        return (index - 1) // 2
        
    @staticmethod
    def _children(index):
        return 2*index +1, 2*index +2
    
    def _is_leaf(self,index):
        child1, _ = BinaryHeap._children(index)
        return child1 >= self._num_elements
        
    
    def _index_min_child(self, index):
        child1, child2 = BinaryHeap._children(index)
        if child2 < self._num_elements:
                return child1 if self._data[child1] < self._data[child2] else child2
        return #iets#

    def __str__(self):
        return str(self._data[:self._num_elements])
    
if __name__ == '__main__':
    heap = BinaryHeap()
    print ("heap is empty: ", heap.is_empty())
    heap.insert_elem(5)
    heap.insert_elem(6)
    heap.insert_elem(8)
    heap.insert_elem(2)
    heap.insert_elem(1)
    print(heap)
    print(heap.remove_min_elem())
    print(heap)