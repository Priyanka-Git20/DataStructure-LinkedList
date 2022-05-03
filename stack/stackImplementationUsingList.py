'''
@Author : Priyanka
@Date : 2022-04-24  5:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-24 6:50:00
@Title :Implementation of the stack using list.
'''


class Stack:
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit

    def push(self,item ):
        if len(self.stack)>= self.limit:
            print("Stack overflow")
        else:
            self.stack.append(item)

    def pop(self):
        if len(self.stack) <= 0:
            print("Stack is underflow")
        else:
            self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def size(self):
        if self.stack:
            return len(self.stack)
        else:
            return None

    def is_empty(self):
        if self.stack == []:
            return True
        else:
            return False

    def display(self):
        print(self.stack)


if __name__ == '__main__':
    mystack = Stack()

    while True:
        choice = int(input("\n 1.push \n 2.pop \n 3.peek \n 4.size \n 5.is_empty \n 6.display \n 7.exit \n Enter your choice :" ))

        if choice == 1:
            item = input("Enter the item")
            mystack.push(item)
        if choice == 2:
            mystack.pop()
        if choice == 3:
            print(mystack.peek())
        if choice == 4:
            print(mystack.size())
        if choice == 5:
            print(mystack.is_empty())
        if choice == 6:
            mystack.display()
        if choice == 7:
            break
