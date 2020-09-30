#!/usr/bin/env pyhton3
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert(self,new_data):
        temp = Node(new_data)
        temp.next = self.head
        self.head = temp

    def insafter(self,pos,ele):
        temp = Node(ele)
        if pos == 1:
            temp.next = self.head
            self.head = temp
        else:
            temp2 = self.head
            for i in range(0,pos-2):
                temp2=temp2.next
            temp.next = temp2.next
            temp2.next = temp

    def append(self,ne):
        temp = Node(ne)
        if self.head == None:
            self.head = temp
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = temp

    def dele(self,pos):
        temp = self.head
        if pos == 1:
            self.head = temp.next
        else:
            for i in range(0,pos-2):
                temp = temp.next
            temp2 = temp.next
            temp.next = temp2.next


    def del_h(self):
        temp = self.head
        self.head = temp.next

    def del_l(self):
        temp = self.head
        if temp.next == None:
            self.head = temp.next
            return
        while temp.next.next:
            temp = temp.next
        temp.next = None


    def pr(self):
        temp = self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next

    def search(self,ele):
        temp = self.head
        count = 0
        while temp:
            count += 1
            if temp.data == ele:
                print("element found at pos {}".format(count))
                return True
            temp = temp.next

        return  False
    def reverse(self):
        current = self.head
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev



    @staticmethod
    def thud():
        print("this is a static method")



if __name__ == '__main__':
    llist = Linked_list()
    llist.insert(4)
    llist.insert(3)
    llist.insert(2)
    llist.insert(1)
    print("appending at head")
    llist.pr()
    print()
    print("Appending after a given point")
    llist.insafter(3,3)
    llist.insafter(1,0)
    llist.pr()
    print()
    print("Deleting an element")
    llist.dele(4)
    llist.pr()
    llist.append(6)
    llist.insert(6)
    print()
    print("Appending at end")
    llist.pr()
    print()
    llist.del_h()
    print("deleting head")
    llist.pr()
    print()
    print("searching an element")
    if llist.search(5):
        print("found")
    else:
        print("not found")
    llist.reverse()
    print("reversed linked list is")
    llist.pr()
    print()
    llist.thud()



