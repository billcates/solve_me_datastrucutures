class DoubleNode:
    def __init__(self,value):
        self.value=value
        self.prev=None
        self.next=None

class LRU_List:
    def __init__(self,head=None):
        self.list={}
        self.head=head
        self.tail=None

    def addFirst(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
        self.list[node.value]=node

    def remove(self,node):
        if node.prev!=None:
            node.prev.next = node.next

        else :
            self.head = node.next

        if node.next != None:
            node.next.prev = node.prev
        else:
            self.tail=node.prev

        del self.list[node.value]
        del node

    def find_Node(self,key):
        return self.list[key]


class LRU_Cache(object):

    def __init__(self, capacity):
        if capacity==0: # when capacity is zero
            print("The given LRU capacity is 0 and cant be processed")
            return
        # Initialize class variables
        self.LRU_capacity=capacity
        self.LRU={}
        self.LRU_list=LRU_List()
        self.LRU_size=0
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.LRU.get(key):
            self.LRU_list.remove(self.LRU_list.find_Node(key))
            self.LRU_list.addFirst(DoubleNode(key))
            return self.LRU[key]
        else:
            return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.LRU_size == self.LRU_capacity:
            del self.LRU[self.LRU_list.tail.value]
            self.LRU_list.remove(self.LRU_list.tail)
            self.LRU_size-=1
        self.LRU[key]=value
        self.LRU_list.addFirst(DoubleNode(key))
        self.LRU_size+=1
        pass




#test cases
our_cache = LRU_Cache(5)

print(our_cache.LRU)
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because key 3 was thrown out
our_cache.set(7, 7)
our_cache.get(4)
print(our_cache.LRU)

#OVERWRITTEN
our_cache1=LRU_Cache(3)
our_cache1.set(1,1)
our_cache1.set(2,2)
our_cache1.set(3,3)
our_cache1.set(4,4)
print(our_cache1.get(4))   #returns= 4
print(our_cache1.get(1))   #returns = -1
our_cache1.set(2,4)
print(our_cache1.get(2)) #returns 4
