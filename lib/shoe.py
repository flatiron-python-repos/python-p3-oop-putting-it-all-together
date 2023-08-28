#!/usr/bin/env python3

class Shoe:    
    def __init__(self, brand, size, condition="New"):
        self.brand = brand
        self.size = size
        self.condition = condition

    def cobble(self):
        print("Your shoe is as good as new!")
    
    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def get_size(self):
        return self._size
    
    # def set_condition(self, condition):
    #     self._condition = condition

    # def get_condition(self):
    #     return self._condition

    size = property(get_size, set_size)
    # condition = property(get_condition, set_condition, "New")