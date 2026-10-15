class Node:
    def __init__(self,value):
        self.prev = None
        self.data = value
        self.next = None
class LinkedList:
        def __init__(self):
             self.head = None


        def append(self,new_node):
             temp = self.head
             if temp:
                  while temp.next:
                       temp = temp.next
                  temp.next = new_node
                  new_node.prev = temp
             else: #First node
                 self.head = new_node

        def insert(self,new_node,pos):
             temp = self.head
             if pos ==1:
                  new_node.next = self.head
                  self.head.prev = new_node
                  self.head = new_node
             else:
                while(p!= pos-1):
                     temp = temp.next
                     p+=1
                temp.next = new_node
                new_node = temp
                new_node.next = temp.next
                if temp.next: # LAST position 
                     temp.next.prev = new_node

                
                  
        def print(self):
             temp = self.head
             print("List elements:")
             while temp:
                 print(temp.data, end = " ")
                 temp=temp.next

list1 = LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.print()

