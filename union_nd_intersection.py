class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
    def __repr__(self):
        return str(self.value)
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.num_elements=0
    def append(self,value):
        if self.head is None:
            new=Node(value)
            self.head=new
            self.tail=new
        else:
            new=Node(value)
            self.tail.next=new
            self.tail=self.tail.next
        self.num_elements+=1
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string+="None"
        return out_string
def union(linkedlist1,linkedlist2):
    if linkedlist1 is None:
        return linkedlist2
    elif linkedlist2 is None:
        return linkedlist1
    output_set=set()
    temp=linkedlist1.head
    while temp is not None:
        output_set.add(temp.value)
        temp=temp.next
    temp=linkedlist2.head
    while temp is not None:
        output_set.add(temp.value)
        temp=temp.next
    union_linkedlist=Linkedlist()
    for each in output_set:
        union_linkedlist.append(each)
    return union_linkedlist
def intersection(linkedlist1,linkedlist2):
        if linkedlist1 is None:
            return None
        elif linkedlist2 is None:
            return None
        list1=[];list2=[]
        temp=linkedlist1.head
        while temp is not None:
            list1.append(temp.value)
            temp=temp.next
        temp=linkedlist2.head
        while temp is not None:
            list2.append(temp.value)
            temp=temp.next
        result=[each for each in list1 if each in list2]
        result_llist=Linkedlist()
        for each in result:
            result_llist.append(each)
        return result_llist
#test case
linkedlist1=Linkedlist()
linkedlist1.append(12)
linkedlist1.append(15)
linkedlist2=Linkedlist()
linkedlist2.append(10)
linkedlist2.append(15)
linkedlist2.append(30)
print(union(linkedlist1,linkedlist2))
print("the length of the union list is")
print(union(linkedlist1,linkedlist2).num_elements)
print(intersection(linkedlist1,linkedlist2))
print("The length of the intersection list is")
print(intersection(linkedlist1,linkedlist2).num_elements)
linkedlist3=Linkedlist()
print("Empty linked list is intersected")
print(intersection(linkedlist1,linkedlist3))
