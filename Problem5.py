import hashlib
import datetime

class Block:

    def __init__(self, data, previous_hash):
        self.index=0
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next=None
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

class Blockchain:
    def __init__(self,primitive_data):
        new=Block(primitive_data,0)
        self.head=new
        self.tail=new

    def append(self,data):
        if self.head is not None:
            new=Block(data,self.tail.hash)
            self.tail.next=new
            self.tail=self.tail.next
    def traverse(self):
        tmp=self.head
        if tmp is None:
            return None
        while tmp is not None:
            print(" Index: "+str(tmp.index))
            print(" Timestamp: "+str(tmp.timestamp))
            print(" data: "+str(tmp.data) +"\n previos hash: "+str(tmp.previous_hash)+"\n current hash: "+str(tmp.hash))
            print("\n\n")
            tmp=tmp.next


#testcases
#
print("empty but block created")
print(" Initial our_block created")
our_block=Blockchain("college")
our_block.traverse()
#initial Block
#adding new elements to Block
print("\n\n\n  one element Block chain")
our_block.append("lecture")
our_block.traverse()
print("\n\n\n after adding two elements")
our_block.append("students")
our_block.traverse()
print("More elements added")
our_block.append("pen")
our_block.append("note")
our_block.append("book")
our_block.traverse()
