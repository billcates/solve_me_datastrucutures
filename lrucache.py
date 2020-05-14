from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity=5):
        # Initialize class variables
        self.capacity=capacity
        self.orderq=deque()
        self.table={}
        self.num_elements=1
        #max size is set to 5
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.table:
            return self.table.get(key)
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.num_elements<=self.capacity:
            if key not in self.table:
                self.table[key]=value
                self.orderq.append(key)
                self.num_elements+=1

        else:
            node=self.orderq.popleft()
            self.table[node]=value

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))
    # returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.table)
