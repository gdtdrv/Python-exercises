class Queue:

    # Constructor creates a list
    def __init__(self):
        self.queue = []

    def __str__(self):
        for each in self.queue:
            return (str(self.queue))

    # Adding elements to stack
    def push(self, data):
        self.queue=[data,*self.queue]

    # Removing elements from a stack
    def pop(self):
        last_element= len(self.queue) -1
        self.queue=self.queue[:last_element]
        print(len(self.queue))

    def IsEmpty(self):
        if len(self.queue)==0:
            return True
        return False

    def clear(self):
        self.queue=[]

myStack = Queue()
print(myStack.push(5))  # prints True
print(myStack.push(6))  # prints True
print(myStack.push(9))  # prints True
print(myStack)
print(myStack.pop())
print(myStack)
print(myStack.IsEmpty())
print(myStack.clear())
print(myStack.IsEmpty())
