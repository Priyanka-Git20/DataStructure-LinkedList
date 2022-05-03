'''
@Author : Priyanka
@Date : 2022-04-24  1:30:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-23 3:50:00
@Title :Implementation of the linkedList.
'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insert_at_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = ne

    def insert_at_postion(self,data,pos):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        # np.data = data
        np.next = temp.next
        temp.next = np

    def deletion_at_begining(self):
        temp = self.head
        self.head = temp.next
        temp.next = None

    def deletion_at_end(self):
        prev = self.head
        temp = self.head.next
        while temp.next is not None:
            temp = temp.next
            prev = prev.next
        prev.next = None

    def deletion_at_position(self,pos):
        prev = self.head
        temp = self.head.next
        for i in range(1,pos-1):
            temp = temp.next
            prev = prev.next
        prev.next = temp.next
        temp.next = None

    def display(self):
        if self.head is None:
            print("Linked list is empty")

        else:
            temp = self.head
            while temp:
                print(temp.data,"---->",end=" ")
                temp = temp.next


if __name__ == '__main__':
    l = SingleLinkedList()
    n1 = Node(10)
    l.head = n1
    n2 = Node(20)
    n1.next = n2
    n3 = Node(40)
    n2.next = n3
    n4 = Node(50)
    n3.next = n4
    #l.delection_at_position(2)

    l.insert_at_end(18)
    # l.insert_begining(25)
    l.insert_at_postion(35, 3)
    # l.deletion_at_begining()
    l.display()


