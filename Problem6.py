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
        list1=set();list2=set()
        temp=linkedlist1.head
        while temp is not None:
            list1.add(temp.value)
            temp=temp.next
        temp=linkedlist2.head
        while temp is not None:
            list2.add(temp.value)
            temp=temp.next
        result=list1.intersection(list2)
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
print("Union is")
print(union(linkedlist1,linkedlist2))#returns 10 -> 12 -> 30 -> 15 -> None
print("the length of the union list is")
print(union(linkedlist1,linkedlist2).num_elements)#returns 4
print("Intersection is")
print(intersection(linkedlist1,linkedlist2))#returns 15 -> None
print("The length of the intersection list is")
print(intersection(linkedlist1,linkedlist2).num_elements)#returns 1
linkedlist3=Linkedlist()
print("Empty linked list is intersected")
print(intersection(linkedlist1,linkedlist3))#returns None
print("Empty linked list union")
linkedlist4=Linkedlist()
linked5=Linkedlist()
print(union(linkedlist4,linked5))#RETURN None
linkedlist4.append(20)
linkedlist4.append(21)
linkedlist4.append(22)
linkedlist4.append(23)
linked5.append(20)
linked5.append(21)
linked5.append(22)
linked5.append(23)
print("if both the linked lists are same\nthe union is")#returns 20 -> 21 -> 22 -> 23 -> None
print(union(linkedlist4,linked5))
print("\nthe intersection is\n",intersection(linkedlist4,linked5))#returns 20 -> 21 -> 22 -> 23 -> None
