class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Linkedlist:
    def __init__(self):
            self.head=None
    def append(self,new_node):
            if self.head==None:
                self.head=new_node
            else:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=new_node
    def del_node(self,value):
        temp=self.head
        prev=None
        #deleting first node
        
        if temp.data==value:
            self.head=self.head.next
            return
        
        while (temp):
            if temp.data==value: # searching value
                break
            else:  #traverse
                prev=temp
                temp=temp.next
        if temp==None:
            print("Value is not present in list")
            return
        prev.next=temp.next
        temp=None
        
   
    def print(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
            
list=Linkedlist()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.append(Node(50))
list.print()
list.del_node(50)
list.print()