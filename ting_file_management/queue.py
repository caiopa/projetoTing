from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)
       
    def dequeue(self):
         if len(self.items) == 0:
            raise IndexError("Queue is empty")
         return self.items.pop(0)
         

    def search(self, index):
        if( 0 <= index <= len(self.items)):
            return self.items[index]
        else: 
            raise IndexError("Item not found in queue")
