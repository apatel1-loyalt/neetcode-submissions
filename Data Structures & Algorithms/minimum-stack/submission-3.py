
class MinStack:

    def __init__(self):
        self.len = 0
        self.arr = []
        

    def push(self, val: int) -> None:
        if (len(self.arr) <= self.len):
            self.arr.append(val)
        else:
            self.arr[self.len] = val
        self.len += 1


    def pop(self) -> None:
        if self.len > 0:
            self.len -= 1
        else:
            self.len = 0

    def top(self) -> int:
        if self.len > 0:
            return self.arr[self.len-1]
        else:
            return null
        

    def getMin(self) -> int:
        min = 0
        if self.len == 0:
            return null
        else:
            min = self.arr[0]
            print(self.arr)
            for i in range(self.len):
                print(self.arr[i])
                if self.arr[i] <= min:
                    min = self.arr[i]
        return min

        
