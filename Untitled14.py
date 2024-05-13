#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#2. stack using arrays
class Stack:
    Stack=[]
    def __init__(self):
        self.top = None
    def is_empty(self):
        return self.top is None
    def push(self, data):
        self.append(data)
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.top()

data = self.top.data
self.top = self.top.next
return data



