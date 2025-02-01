class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
# Create a queue
my_queue = Queue()

# Add elements to the queue
my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)

print("Queue: ", my_queue.queue)

# Dequeue elements from the queue  
print("Dequeue: ", my_queue.dequeue())

print("Queue: ", my_queue.queue)

# Peek at the front of the queue
print("Peek: ", my_queue.peek())

# Check if the queue is empty
print("Is Queue empty? ", my_queue.is_empty())

# Get the size of the queue
print("Size of the queue: ", my_queue.size())