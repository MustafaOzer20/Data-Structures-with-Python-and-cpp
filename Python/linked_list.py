class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkedList:
    __counter = 0
    def __init__(self, *args):
        self.head = None # first item
        self.tail = None # last item
        for arg in args:
            self.append(arg)

    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        self.__counter += 1

    def insert(self, data, index):
        if (0 <= index) & (index <= self.__counter - 1):
            if index == self.__counter - 1:
                self.append(data)
            else:
                node = Node(data)
                if index == 0:
                    node.next = self.head
                    self.head = node
                else:
                    temp = self.head
                    i = 0
                    attr = temp
                    while i<index:
                        attr = temp
                        temp = temp.next
                        i += 1
                    # index - 1 attr, index temp ;
                    #  ... -> attr -> node -> temp -> ... 
                    attr.next = node
                    node.next = temp
                    self.__counter += 1
        else:
            raise IndexError("list index out of range")

    def delete(self, index):
        if self.head != None:
            if (0 <= index) & (index <= self.__counter - 1):
                temp = self.head
                if index == 0:
                    self.head = temp.next
                elif index == self.__counter - 1:
                    j = 0
                    while j<self.__counter-2:
                        temp = temp.next
                        j+=1
                    self.tail = temp
                    self.tail.next = None
                else:
                    i = 0
                    while i < index:
                        attr = temp
                        temp = temp.next
                        i += 1
                    temp = temp.next
                    attr.next = temp

                self.__counter -= 1
            else:
                raise IndexError("list index out of range")
        else:
            raise IndexError("del from empty list")
    
    def __iter__(self):  # for i in object
        if self.head != None:
            temp = self.head
            while temp != None:
                val = temp.data
                temp = temp.next
                yield val
        else:
            print("[]")

    def __find_item(self, indices, get_or_set): # __find_item(3, "get")
        if indices < 0:
            indices = self.__counter + indices
        if 0 <= indices < self.__counter:
            temp = self.head
            for i in range(self.__counter):
                if i == indices:
                    if get_or_set == "get":
                        return temp.data
                    elif get_or_set == "set":
                        return temp
                temp = temp.next
        else:
            raise IndexError("que index out of range")


    def __getitem__(self, indices): # object[index]
        val = self.__find_item(indices, "get")
        return val

    def __setitem__(self, indices, newVal): # object[index] = newVal
        temp = self.__find_item(indices, "set")
        temp.data = newVal

    def __len__(self):   # len(object)
        return self.__counter

    def __str__(self):  # print(object)
        printList = ""
        j = 0
        for i in self:
            if j != len(self)-1:
                printList += str(i) + " -> "
            else:
                printList += str(i)
            j += 1
        return printList


