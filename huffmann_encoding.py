
import sys
import operator

def process(org):
    d={}
    s=list(org)
    a=set(s)
    a=list(a)
    for i in a:
        d[i]=s.count(i)
    d=sorted(d.items(),key=operator.itemgetter(1))
    return d

class Node:
    def __init__(self, data=None,count=None):
        self.data= data
        self.freq= count
        self.right=None
        self.left=None
class HuffmanTree:
    def __init__(self):
        self.head=None
    def path_from_root_to_node(self,data):

        output = self.path_from_node_to_root(self.head,data)
        return output[::-1]

    def path_from_node_to_root(self,node,data):

        if node is None:
            return None

        elif node.data == data:
            return ''

        left_answer = self.path_from_node_to_root(node.left, data)
        if left_answer is not None:
            left_answer+='0'
            return left_answer

        right_answer = self.path_from_node_to_root(node.right, data)
        if right_answer is not None:
            right_answer+='1'
            return right_answer
        return None
def encode(d):
    tree=HuffmanTree()
    check=[]
    if len(data)==0:
        return '',tree
    if len(d)==1:
        a=list(d[0])
        tree.head=Node(a[0],1)
        return tree
    while len(d)>1:
        a=list(d[0])
        b=list(d[1])
        if len(a[0])==1:
            new1=Node()
            new1.data=a[0]
            new1.freq=a[1]
        else:
            new1=check[0]
            del check[0]
        if len(b[0])==1:
            new2=Node()
            new2.data=b[0]
            new2.freq=b[1]
        else:
            new2=check[0]
            del check[0]
        new3=Node()
        new3.freq=new2.freq+new1.freq
        new3.data=new2.data+new1.data
        if new2.freq>=new1.freq:
            new3.left=new1
            new3.right=new2
        else:
            new3.left=new2
            new3.right=new1
        tree.head=new3
        check.append(new3)
        d=dict(d)
        d[tree.head.data]=tree.head.freq
        d=list(sorted(d.items(),key=operator.itemgetter(1)))
        del d[0]
        del d[0]
    return tree
def encoded_values(data):
        d=process(data)
        if len(data)==0:
           return '',encode(data)
        if len(d)==1:
            value="0"
            return value,encode(d)
        root=encode(d)
        value=""
        for i in data:
             value+=root.path_from_root_to_node(i)
        return value,root
def decode(data,tree):
    decoded_data=''
    if len(data)==0:
        return ''
    if len(data)==1:
        return tree.head.data
    current=tree.head
    for x in data:
        if x=='0':
            current=current.left
        elif x=='1':
            current=current.right

        if current.left==None and current.right==None:
                decoded_data+=current.data
                current=tree.head
    return decoded_data

print("\nTestcase:1")
data="I"
print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
print ("The content of the data is: {}\n".format(data))
encoded_data,root=encoded_values(data)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data=decode(encoded_data,root)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


print("\nTestcase:2")
data=""
print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
print ("The content of the data is: {}\n".format(data))
encoded_data,root=encoded_values(data)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof((encoded_data))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data=decode(encoded_data,root)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


print("\nTestcase:3")
data="AAAAAAABBBCCCCCCCDDEEEEEE"
print ("The size of the data is: {}\n".format(sys.getsizeof(data)))
print ("The content of the data is: {}\n".format(data))
encoded_data,root=encoded_values(data)
print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))
decoded_data=decode(encoded_data,root)
print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))
