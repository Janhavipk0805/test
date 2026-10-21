# singly linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# creating linked list using append
def append(self,data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return
    temp = self.head

    while temp.next is not None:
        temp = temp.next
        temp.next = new_node

# traverse and print node values
def display(self):
   temp = self.head

   if temp is None:
    print("Invalid position")
    return

   if temp is not None:
       print(temp.data,end = " ->")
       temp = temp.next
       print("None")

# Insert node at specific position
def insert(self,data,pos):
    new_node = Node(data)

    if pos <1:
        print("Invalid position")
        return

    if pos ==1:
        new_node.next = self.head
        self.head = new_node
        return
    temp = self.head
    count =1

    while temp is not None and count < pos-1:
        temp = temp.next
        count +=1

    if temp is None:
        print("Invalid position")
        return

    new_node.next = temp.next
    temp.next = new_node

# delete alternate nodes
def delete_alternate(self):
    temp = self.head()

    while temp is not None and temp.next is not None:
        temp.next = temp.next.next
        temp = temp.next

# main program
ll = LinkedList()

#create linked list
values = input("Enter node values separated by spaces:").split()

for value in values:
      ll.append(int(value))


print("\n Original linked list:")
ll.display()

#Insert a node
data = int(input("\n Enter value to insert:"))
position = int(input("Enter position to insert:"))

ll.insert(data,position)
print("\n After insertion")
ll.display()


#Delete alternate nodes
ll.delete_alternate()

print("\n After deleting alternate nodes:")
ll.display()

#main program
ll = LinkedList()

# create linked list
values = input("enter node values using spaces:").split()

for value in values:
    ll.append(int(value))

print("\n Original linked list:")
ll.display()

# Insert a node
data = int(input("\n Enter value in the linked list:"))
position= int(input("\n Enter position to be inserted"))
ll.insert(data,position)

print("\n After insertion")
ll.display()

#Delete alternate nodes
ll.delete_alternate()

print("\n After deleting alternate nodes:")
ll.display()