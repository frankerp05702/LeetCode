import random

class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False
        self.nums.append(val)
        self.index_map[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False
        last_element, idx = self.nums[-1], self.index_map[val]
        self.nums[idx], self.index_map[last_element] = last_element, idx
        self.nums.pop()
        del self.index_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Example usage:
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3 = obj.insert(2)
# param_4 = obj.getRandom()
# param_5 = obj.remove(1)
# param_6 = obj.insert(2)
# param_7 = obj.getRandom()
