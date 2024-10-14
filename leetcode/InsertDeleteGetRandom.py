# https://leetcode.com/problems/insert-delete-getrandom-o1


import random


class RandomizedSet:
    def __init__(self):
        self.arr = {}

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr[val] = val
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        res = key, val = random.choice(list(self.arr.items()))
        return val
