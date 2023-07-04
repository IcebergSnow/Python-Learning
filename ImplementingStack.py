class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, num):
        self.stack_list.append(num)
    def pop(self):
        return_number = self.stack_list[-1]
        del self.stack_list[-1]
        return return_number
