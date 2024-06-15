class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end='->')
            temp = temp.next
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def prepand(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self,data):
        if self.head==None:
            return
        if self.head.data==data:
            self.head = self.head.next
            return
        
        temp=self.head
        prev=None
        while temp.next:
            
            if temp.data == data:
                prev.next=temp.next
            prev=temp
            temp=temp.next
    

if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(4)
    ll.append(5)
    ll.append(2)
    ll.prepand(0)
    ll.delete_with_value(4)
    ll.printList()