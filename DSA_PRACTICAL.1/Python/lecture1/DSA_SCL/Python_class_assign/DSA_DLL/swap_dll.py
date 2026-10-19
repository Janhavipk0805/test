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
        def print(self):
             temp = self.head
             print("\nList elements:\n")
             while temp:
                 print(temp.data, " ")
                 temp=temp.next
        def count_occ(self,num):
             temp = self.head
             cnt = 0
             while  temp:
                  if temp.data == num:
                       cnt += 1
                  temp = temp.next
             print(" The occurence:", cnt)

        def swap(self):
             temp = node1 = self.head  # node1 is first node
             while temp.next: # temp is last node
                  temp = temp.next
             temp.next = node1.next
             node1.next = None
             node1.prev = temp.prev
             temp.prev.next = node1
             temp.prev = None
             self.head = temp

       

list1 = LinkedList()
list1.append(Node(12))
list1.append(Node(52))
list1.append(Node(102))
list1.append(Node(56))
list1.print()
list1.swap()
list1.print()

