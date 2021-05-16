class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Queue:
    __counter = 0
    def __init__(self, *args):
        self.head = None
        self.tail = None
        for arg in args:
            self.enqueue(arg)

    def enqueue(self, data):
        temp = Node(data)
        if self.tail == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.__counter += 1

    def dequeue(self):
        if self.head == None:
            raise Exception("Queue is empty")
        else:
            val = self.head.data
            temp = self.head.next
            self.head = temp
            self.__counter -= 1
            return val

    def __iter__(self):  # for i in object
        if self.head == None:
            print("[]")
        else:
            temp = self.head
            while temp != None:
                val = temp.data
                temp = temp.next
                yield val

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
        

    def __len__(self): # len(object)
        return self.__counter

    def __str__(self): # print(object)
        printQueue = ""
        j = 1
        for i in self:
            if j != len(self):
                printQueue += str(i) + " -> "
            else:
                printQueue += str(i)
            j += 1
        return printQueue
    




