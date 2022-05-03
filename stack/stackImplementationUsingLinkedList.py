'''
@Author : Priyanka
@Date : 2022-04-23  7:10:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-23 7:50:00
@Title :Implementation of the linkedList.
'''


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    def pop(self):
        if self.isempty():
            print("Underflow condition")
        else:
            popnode = self.head
            self.head = self.head.next
            popnode.next = None
            return popnode.data

    def peek(self):
        if self.isempty():
            return None
        else:
            return self.head.data

    def display(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end=" ")
                temp = temp.next

if __name__ == '__main__':
    mystack = Stack()
    mystack.push(12)
    mystack.push(14)
    mystack.push(20)
    print(mystack.display())
    print(mystack.peek())
    mystack.pop()
    print(mystack.display())