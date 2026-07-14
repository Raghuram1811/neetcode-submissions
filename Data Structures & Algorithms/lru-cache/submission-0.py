class Node:

    def __init__(self, key, value):

        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def insert_at_front(self, node):
        right_node = self.head.next  # Step 1: Save the original second node

        # Step 2: Connect the new node to the head
        node.prev = self.head
        self.head.next = node        # MISSING IN YOUR ORIGINAL CODE

        # Step 3: Connect the new node to the right node
        node.next = right_node
        right_node.prev = node


    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert_at_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        node = Node(key, value)
        self.cache[key] = node
        self.insert_at_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]




        
