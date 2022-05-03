'''
@Author : Priyanka
@Date : 2022-04-24  4:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-24 5:00:00
@Title :Implementation of the queue using list.
'''

class Queue:
    def __init__(self,limit = 10):
        self.queue = []
        self.limit = limit

    def enqueue(self,item ):
        if len(self.queue)>= self.limit:
            print("Queue is  overflow")
        else:
            self.queue.append(item)

    def dequeue(self):
        if len(self.queue) <= 0:
            print("Stack is underflow")
        else:
            self.queue.pop(0)

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def size(self):
        if self.queue:
            return len(self.queue)
        else:
            return None

    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False

    def display(self):
        print(self.queue)


if __name__ == '__main__':
    myqueue = Queue()

    while True:
        choice = int(input("\n 1.enque \n 2.dequeue \n 3.peek \n 4.size \n 5.is_empty \n 6.display \n 7.exit \n Enter your choice :" ))

        if choice == 1:
            item = input("Enter the item")
            myqueue.enqueue(item)
        if choice == 2:
            myqueue.dequeue()
        if choice == 3:
            print(myqueue.peek())
        if choice == 4:
            print(myqueue.size())
        if choice == 5:
            print(myqueue.is_empty())
        if choice == 6:
            myqueue.display()
        if choice == 7:
            break


