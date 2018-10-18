#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 19:32:30 2018
@author: tan
"""

class Fib(object):
    def __init__(self):
        pass
    def s1(self, num):
        if num < 2:
            return num
        return self.s1(num- 1) + self.s1(num - 2)
    
    
if __name__ == '__main__':
    man = Fib()
    print(man.s1(5))
