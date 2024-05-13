#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#3. queues using arrays, enqueue,dequeue and peek
calss Queue:
    Queue=[]
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            print("Queue is empty")
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        self.front = self.front.next
        ifself.frontisNone:
        self.rear = None
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.top.data

        
        
        
        
        
        
        
        
        



