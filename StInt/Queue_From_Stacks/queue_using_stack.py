class Stack(object):
  def __init__(self):
    self.container = list()
  
  def push(self, value):
    self.container.append(value)
  
  def pop(self):
    if self.container:
      return self.container.pop()
    else:
      return None

class Queue(object):
  def __init__(self):
    self.queue = Stack()
    self.backup_stack = Stack()

  def enqueue(self, value):
    if self.queue.container:
      self.queue.push(value)
    else:
      if self.backup_stack.container:
        while self.backup_stack.container:
          print "Enqueueing"
          self.queue.push(self.backup_stack.pop())
      self.queue.push(value)

  def dequeue(self):
    while self.queue.container:
      self.backup_stack.push(self.queue.pop())
    return self.backup_stack.pop()


def main():
  queue_one = Queue()
  queue_one.enqueue(1)
  queue_one.enqueue(2)
  queue_one.enqueue(3)
  queue_one.enqueue(4)
  print queue_one.dequeue() 
  print queue_one.dequeue()
if __name__ == "__main__":
  main()   
