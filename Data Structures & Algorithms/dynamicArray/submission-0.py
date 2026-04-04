class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0 # is the length of the array with members
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    # Overriding the value at ith index 
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    # Adding member at the end of the array 
    def pushback(self, n: int) -> None:
        # if we reach the end of the capacity
        if self.capacity == self.size:
            self.resize()

        # Adding the member at the end
        self.arr[self.size] = n
        self.size += 1

    # Removing member at the end of the array
    def popback(self) -> int:

        # Decrease the size of the array
        self.size -= 1

        return self.arr[self.size]
 

    # As mentioned in the Question
    # We double the capacity
    def resize(self) -> None:
        
        # Double the capacity
        self.capacity *= 2

        # New Array 
        new_arr = [0] * self.capacity

        # Coping older members
        for i in range(self.size):

            new_arr[i] = self.arr[i]
            
        # Moving newer array as the current one
        self.arr = new_arr


    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
