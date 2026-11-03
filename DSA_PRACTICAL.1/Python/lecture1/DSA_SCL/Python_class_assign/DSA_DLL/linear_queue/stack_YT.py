class stack:
    def __init__(self):
        self.s = []
    def length(self):
        return len(self.s)
    def push(self,value):
        self.s.insert(0,value)
    def push(self,value):
        self.s.insert(0,value)
    def peek(self):
        if len(self.s) ==0:
            raise Exception()