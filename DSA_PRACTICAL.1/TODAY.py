class Node:
    def __init__(self,val):
        self.data = val #store the value in node
        self.next = None #next node address is none


class LinkedList:
    def reverse(self, prev): #reversing a linked list
        self.head =prev
    def findmid_del(self):
        temp = temp1= self.head
        prev = None
        while temp1 and temp1.next:
            prev = temp
            while temp1 and temp1.next:
                prev = temp
                temp = temp.next
                temp1 = temp1.next.next
            print("Middle node:",temp.data)
            prev.next = temp.next
            temp = None
    def delfirst_last(self):
        temp1=self.head
        temp1= None
        prev = None
        temp = self.head = self.head.next
        while(temp.next):
            prev = temp
            temp = temp.next
        prev.next = None
        temp = None
    def print(self):
        print("List elements:")
       