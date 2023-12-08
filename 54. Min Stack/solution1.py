class MinStack:

    def __init__(self):
        self.items = []
        self.min = 2**31

    def push(self, val: int) -> None:
        if val == None: return
        if val < -(2**31) or val >= 2**31: return
        self.items.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        if not self.items: return
        popped = self.items.pop(-1)
        if popped not in self.items and popped == self.min:
            if self.items: self.min = min(self.items)
            else: self.min = 2**31

    def top(self) -> int:
        return self.items[-1] if self.items else None

    def getMin(self) -> int:
        return self.min if self.min < 2**31 else None


# # Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin()) # return -3
# obj.pop()
# print(obj.top())    # return 0
# print(obj.getMin()) # return -2

obj = MinStack()
cmds = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
args = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
result = [None]
expected = [None,None,None,None,2147483647,None,2147483646,None,2147483646,None,None,2147483647,2147483647,None,-2147483648,-2147483648,None,2147483647]
for i, cmd in enumerate(cmds):
    arg = None
    if len(args[i]) > 0:
        arg = args[i][0]
    match cmd:
        case "push":
            result.append(obj.push(arg))
        case "pop":
            result.append(obj.pop())
        case "top":
            result.append(obj.top())
        case "getMin":
            result.append(obj.getMin())
print(result)
print(expected)
print(result == expected)

# cmds = ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
# args = [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
# result = [None]
# expected = [None,None,None,None,None,0,None,0,None,0,None,2]
# for i, cmd in enumerate(cmds):
#     arg = None
#     if len(args[i]) > 0:
#         arg = args[i][0]
#     match cmd:
#         case "push":
#             result.append(obj.push(arg))
#         case "pop":
#             result.append(obj.push(arg))
#         case "top":
#             result.append(obj.top())
#         case "getMin":
#             result.append(obj.getMin())
# print(result)
# print(expected)
# print(result == expected)