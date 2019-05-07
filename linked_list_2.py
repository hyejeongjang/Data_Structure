#연결리스트 노드 삭제하기

class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        if pos<1 or pos>self.nodeCount:
            raise IndexError
        else:
            curr=self.getAt(pos)
            prev=self.getAt(pos-1)
            if self.nodeCount==1: #유일한 노드 삭제
                self.head=None
                self.tail=None
            elif curr.next is None: # 맨 끝 노드 삭제
                self.tail=prev
                self.tail.next=None
            elif prev i None: # 맨 앞 노드 삭제
                self.head=curr.next
            else: # 나머지
                prev.next=curr.next

            self.nodecount-=1
            return curr.data




    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0
