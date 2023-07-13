class IntArray:
    def __init__(self, size):
        self.array_list = []
        self.size = size
        for i in range(1, size+1):
            self.array_list.append(None)
    def assign (self, index, num):
        if index >= self.size or index < 0:
            raise Exception ("Cannot assign value to nonexistent space")
        self.array_list[index] = num
    def change_length (self, new_size):
        if new_size < 0:
            raise Exception ("Size cannot be less than 0")
        new_array = []
        for i in range(1, new_size+1):
            if i > self.size:
                new_array.append(None)
            else:
                new_array.append(self.array_list[i-1])
        self.array_list = new_array
        self.size = new_size
