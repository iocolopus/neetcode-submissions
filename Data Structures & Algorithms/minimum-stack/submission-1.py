class MinStack:

    def __init__(self):
        self.tuple_list = []
        

    def push(self, val: int) -> None:

        if not self.tuple_list:
            self.tuple_list.append((val, val))
        else:
            self.tuple_list.append((val, min(val, self.tuple_list[-1][1])))

    def pop(self) -> None:
        
        self.tuple_list.pop()

    def top(self) -> int:

        return self.tuple_list[-1][0]
        

    def getMin(self) -> int:
        
        return self.tuple_list[-1][1]