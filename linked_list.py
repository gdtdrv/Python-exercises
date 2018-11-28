class Node:
    def __init__(self, content=None, next=None):
        self.content = content
        self.next = next

    def __repr__(self):
        return(str(self.content))

class LinkedList:
    def __init__(self):
        self.head = None
        pass

    def add_element(self, node):
        if self.head==None:
            self.head=node
            self.next=node.next
            self.index=0
        else:
            self.index=1+self.index

    def pprint(self):
        cur_node = self.head
        while cur_node.next!=None:
            print(cur_node.content)
            cur_node = cur_node.next
        print(cur_node.content)

    def pop(self):
        cur_node = self.head
        while cur_node.next!=None:
            pre_node = cur_node
            cur_node=cur_node.next
        self.index=self.index-1
        pre_node.next=None

    def remove(self):
        self.head=None
        self.index=None

    def size(self):
        if self.index!= None:
            print(int(self.index+1))
        else:
            return print('Empty')


node1 = Node(1)
node2 = Node(5)
node3 = Node(37)
node1.next = node2
node2.next = node3

ll = LinkedList()
ll.add_element(node1)
ll.add_element(node2)
ll.add_element(node3)
ll.pprint()
ll.pop()
ll.size()
ll.pop()
ll.size()
ll.remove()
ll.size()





