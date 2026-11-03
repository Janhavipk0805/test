# Q2. Linear Queue with Enqueue, Dequeue, Display, Reverse using Stack,
#     Merge two queues, Check if two queues are identical
# A queue works on FIFO (First In First Out) - the first item added is the first one removed.

class Queue:
    def __init__(self):
        # empty list to store queue elements
        # index 0 = FRONT of the queue, last index = REAR of the queue
        self.items = []

    def is_empty(self):
        # queue is empty when the list has no elements
        return len(self.items) == 0

    # ---------- 1. Enqueue ----------
    def enqueue(self, value):
        # insert the new element at the rear (end of the list)
        self.items.append(value)

    # ---------- 2. Dequeue ----------
    def dequeue(self):
        # if the queue is empty we cannot remove anything (queue underflow)
        if self.is_empty():
            print("Queue Underflow! Queue is empty")
            return None
        # remove and return the element at the front (index 0)
        return self.items.pop(0)

    # ---------- 3. Display ----------
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        print("Queue (front to rear):", end=" ")
        for item in self.items:
            print(item, end=" ")
        print()

    # ---------- 4. Reverse the queue using a stack ----------
    def reverse(self):
        stack = []                              # a stack made using a list
        # take every element out from the front of the queue and push it on the stack
        while not self.is_empty():
            stack.append(self.dequeue())
        # pop from the stack (last in comes out first) and enqueue back
        # so the queue now has the elements in reverse order
        while len(stack) > 0:
            self.enqueue(stack.pop())
        print("Queue reversed")


# ---------- 5. Merge two queues into one ----------
def merge(q1, q2):
    merged = Queue()                 # a new empty queue for the result
    for item in q1.items:            # first add all elements of queue 1
        merged.enqueue(item)
    for item in q2.items:            # then add all elements of queue 2
        merged.enqueue(item)
    return merged


# ---------- 6. Check if two queues are identical ----------
def is_identical(q1, q2):
    # queues with different sizes can never be identical
    if len(q1.items) != len(q2.items):
        return False
    # compare element by element (same position must have the same value)
    for i in range(len(q1.items)):
        if q1.items[i] != q2.items[i]:
            return False
    return True


def read_queue():
    # helper: take elements from the user and make a queue
    q = Queue()
    values = input("Enter elements separated by space: ").split()
    for v in values:
        q.enqueue(v)
    return q


# ---------------- Main program (menu) ----------------
queue1 = Queue()                     # the main queue used for operations 1 to 4

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Reverse the queue using stack")
    print("5. Merge two queues into one")
    print("6. Check if two queues are identical")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter value to enqueue: ")
        queue1.enqueue(value)
        print(value, "enqueued")

    elif choice == "2":
        removed = queue1.dequeue()
        if removed is not None:
            print("Dequeued element:", removed)

    elif choice == "3":
        queue1.display()

    elif choice == "4":
        queue1.reverse()
        queue1.display()

    elif choice == "5":
        print("Enter elements of the first queue")
        a = read_queue()
        print("Enter elements of the second queue")
        b = read_queue()
        result = merge(a, b)
        print("Merged queue:")
        result.display()

    elif choice == "6":
        print("Enter elements of the first queue")
        a = read_queue()
        print("Enter elements of the second queue")
        b = read_queue()
        if is_identical(a, b):
            print("Both queues are identical")
        else:
            print("Queues are NOT identical")

    elif choice == "7":
        print("Program ended")
        break

    else:
        print("Invalid choice, try again")