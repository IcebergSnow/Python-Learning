class FIFO:
    def __init__(self, size):
        self.size = size
        self.fifo_list = [None]*self.size
        self.oldest_index = 0
        self.next_available_index = 0
    def enqueue (self, num):
        if self.oldest_index == self.next_available_index and self.fifo_list[self.oldest_index] != None:
            raise Exception ("Queue is full")
        self.fifo_list[self.next_available_index] = num
        if self.next_available_index == self.size-1:
            self.next_available_index = 0
        else:
            self.next_available_index += 1
    def dequeue(self):
        if self.fifo_list[self.oldest_index] == None:
            raise Exception("No element exists to dequeue")
        return_num = self.fifo_list[self.oldest_index]
        self.fifo_list[self.oldest_index] = None
        if self.oldest_index == self.size-1:
            self.oldest_index = 0
        else:
            self.oldest_index += 1
        return return_num
