from random import choice
class RandomizedSet:

    def __init__(self):
        self.randomset_map = {}
        #self.queue = deque()
        self.list = []


    def add_to_queue(self,Node):
        if self.queue_head == self.queue_tail:
            self.queue_head.next = Node
            Node.prev = self.queue_head
            self.queue_tail = Node
        else:
            firstnode = self.queue_head.next
            self.queue_head.next = Node
            Node.prev = self.queue_head
            Node.next = firstnode
            firstnode.prev = Node
        return

    
    def remove_from_queue(self, Node):
        if self.queue_tail == Node:
            previous = Node.prev
            previous.next = None
            del(Node)
            self.queue_tail = previous
        else:
            previous = Node.prev
            nextnode = Node.next
            previous.next = nextnode
            nextnode.prev = previous
            del(Node)
        return
        

    def insert(self, val: int) -> bool:
        if val in self.randomset_map.keys():
            return False
        self.list.append(val)
        self.randomset_map[val] = len(self.list) -1
        #print(f"final list after insert: {self.list}")
        #self.add_to_queue(value_node)
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.randomset_map.keys():
            #self.remove_from_queue(self.randomset_map[val])
            #n = len(self.list)
            last_index_element = self.list[-1]
            #print(f"last element then = {self.list[-1]}")
            self.list[-1] = val
            #print(f"last element now = {self.list[-1]}")
            actual_index = self.randomset_map[val]
            self.list[actual_index] = last_index_element
            self.randomset_map[last_index_element] = actual_index
            #print(f"actual index element now = {self.list[actual_index]}")
            self.list.pop()
            #print(f"final list after remove: {self.list}")
            self.randomset_map.pop(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return choice(self.list)
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()