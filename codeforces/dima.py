class Node:
    def __init__(self, d):
        self.data = d
        self.next = None
        self.bottom = None

def merge(l1, l2):
    dummy = Node(-1)
    temp = dummy

    while l1 and l2:
        if l1.data < l2.data:
            temp.bottom = l1
            l1 = l1.bottom
        else:
            temp.bottom = l2
            l2 = l2.bottom
        temp = temp.bottom

    if l1:
        temp.bottom = l1
    else:
        temp.bottom = l2

    return dummy.bottom

def flatten(root):
    if not root or not root.next:
        return root
    
    # Recursively flatten the list
    root.next = flatten(root.next)
    
    # Merge this list with the next list
    root = merge(root, root.next)
    
    return root

def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.bottom
    print()

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        head = None
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre = None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m -= 1
            a1 = listo[it]
            it += 1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1

            for j in range(m):
                a = listo[it]
                it += 1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB

        root = flatten(head)
        printList(root)
        t -= 1
