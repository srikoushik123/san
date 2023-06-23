class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        Laste = self.headval
        while Laste.nextval:
            Laste = Laste.nextval
        Laste.nextval = NewNode

    def listprint(self):
        Printval = self.headval
        while Printval is not None:
            print(Printval.dataval)
            Printval = Printval.nextval

List = SLinkedList()
List.headval = Node("Mon")
E2 = Node("Tue")
E3 = Node("Wed")

List.headval.nextval = E2
E2.nextval = E3

List.AtEnd("Thu")
List.listprint()
