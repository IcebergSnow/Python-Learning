list = [1, 4, 7, 10]
def search(value, sorted_list):
    max = len(sorted_list)-1
    min = 0
    while min <= max:
        middle = (max + min) // 2
        if value == sorted_list[middle]:
            return middle
        if value > sorted_list[middle]:
            min = middle+1
        else:
            max = middle-1
    raise Exception("Item does not exist")

