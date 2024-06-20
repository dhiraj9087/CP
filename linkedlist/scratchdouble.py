# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node
#         new_node.prev = last_node

#     def prepend(self,data):
#         new_node = Node(data)
#         if self.head==None:
#             self.head=new_node
#             return
#         self.head.prev=new_node
#         new_node.next=self.head
#         self.head = new_node

#     def delete(self, data):
#         curr_node = self.head
#         # last = None
#         while curr_node:
#             if curr_node.data == data:
#                 if curr_node.prev:
#                     curr_node.prev.next = curr_node.next
#                 else:
#                     self.head = curr_node.next
#                 if curr_node.next:
#                     curr_node.next.prev = curr_node.prev

#             # last = curr_node
#             curr_node = curr_node.next
    
        
n=input().strip()
d={}
# s='abcdefghijklmnopqrstuvwxyz'
