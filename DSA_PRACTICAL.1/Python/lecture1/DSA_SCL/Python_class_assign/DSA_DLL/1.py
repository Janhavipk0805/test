# Q1. Stack with Push, Pop, Display, Reverse String, Reverse Stack
# A stack works on LIFO (Last In First Out) - the last item pushed is the first one popped.

class Stack:
    def __init__(self):
        # create an empty list to store the stack elements
        # the END of the list is the TOP of the stack
        self.items = []

    def is_empty(self):
        # stack is empty when the list has no elements
        return len(self.items) == 0

    # ---------- 1. Push ----------
    def push(self, value):
        # add the new element at the top (end of the list)
        self.items.append(value)
        print(value, "pushed into the stack")

    # ---------- 2. Pop ----------
    def pop(self):
        # if the stack is empty we cannot pop (stack underflow)
        if self.is_empty():
            print("Stack Underflow! Stack is empty")
            return None
        # remove and return the top element
        return self.items.pop()

    # ---------- 3. Display ----------
    def display(self):
        if self.is_empty():
            print("Stack is empty")
            return
        print("Stack (top to bottom):")
        # print from the last element (top) to the first element (bottom)
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i])

    # ---------- 4. Reverse a string using stack ----------
    def reverse_string(self, text):
        temp = Stack()                 # use a new stack so our main stack is not disturbed
        for ch in text:
            temp.push_silent(ch)       # push every character one by one
        reversed_text = ""
        while not temp.is_empty():
            reversed_text = reversed_text + temp.pop()   # pop gives characters in reverse order
        return reversed_text

    def push_silent(self, value):
        # same as push but without printing (used inside other functions)
        self.items.append(value)

    # ---------- 5. Reverse the stack using another stack ----------
    def reverse_stack(self):
        another = Stack()              # the second (helper) stack
        # pop every element from the main stack and push it into the other stack
        # the order gets reversed during this transfer
        while not self.is_empty():
            another.push_silent(self.pop())
        # the other stack now holds the reversed stack, so make it the main stack
        self.items = another.items
        print("Stack reversed")


# ---------------- Main program (menu) ----------------
s = Stack()

while True:
    print("\n----- STACK MENU -----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using another Stack")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to push: ")
        s.push(value)

    elif choice == "2":
        removed = s.pop()
        if removed is not None:
            print("Popped element:", removed)

    elif choice == "3":
        s.display()

    elif choice == "4":
        text = input("Enter a string: ")
        print("Reversed string:", s.reverse_string(text))

    elif choice == "5":
        s.reverse_stack()
        s.display()

    elif choice == "6":
        print("Program ended")
        break

    else:
        print("Invalid choice, try again")