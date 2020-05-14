from collections import deque
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {} #create empty cache using a Python Dictionary
        self.cache_access_history = deque() #deque for doubly linked list
        self.cap = capacity #set initial capacity


    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cap == 0:
          return None
        if key in self.cache.keys():
            temp = self.cache[key]
            del self.cache[key]
            #update last used key in cache history
            self.cache_access_history.appendleft(key) #push most recent key
            if len(self.cache_access_history) > self.cap:
              self.cache_access_history.pop() #delete oldest key from history
            return temp
        else:
            return -1

    #code for testing LRU Cache

    def set(self, key, value):
      if self.cap == 0:
          return None
      if  key in self.cache.keys():
        #only need to update last used key in cache history
        self.cache_access_history.appendleft(key) #push most recent key
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history
        # Set the value if the key is not present in the cache.
        #If the cache is at capacity remove the oldest item.
      elif  key not in self.cache.keys() and len(self.cache)< self.cap:
        self.cache[key] = value #add key, value pair to cache
        #update last used
        self.cache_access_history.appendleft(key)
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history

      elif key not in self.cache.keys() and len(self.cache)==self.cap:
        old = self.cache_access_history.pop() #delete oldest key from history
        self.cache.pop(old) #delete oldest item from cache
        self.cache[key] = value #add key, value pair to cache
        self.cache_access_history.appendleft(key) #update last key used
        if len(self.cache_access_history) > self.cap:
          self.cache_access_history.pop() #delete oldest key from history


our_cache = LRU_Cache(5)

print(our_cache.cache)
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
print(our_cache.cache)
