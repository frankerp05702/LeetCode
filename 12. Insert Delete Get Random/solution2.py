from typing import List
import random

class RandomizedSet:
    def __init__(self):
        self.rset={}
        self.set_length=0

    def insert(self, val: int) -> bool:
        if val in self.rset.keys():
            return False
        else:
            self.rset[val]=val
            self.set_length+=1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.rset.keys():
            return False
        else:
            del self.rset[val]
            self.set_length-=1
            return True

    def getRandom(self) -> int:
        val = random.randint(0,self.set_length-1)
        return self.rset[list(self.rset.keys())[val]]
                    

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

# Example 1:

randomizedSet = RandomizedSet();
print(randomizedSet.insert(1))
print(randomizedSet.remove(2))
print(randomizedSet.insert(2))
print(randomizedSet.insert(3))
print(randomizedSet.getRandom())
print(randomizedSet.remove(1))
print(randomizedSet.insert(2))
print(randomizedSet.getRandom())
 