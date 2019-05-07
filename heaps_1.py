#최대 힙에 새로운 원소를 삽입

class MaxHeap:

    def __init__(self):
        self.data = [None]


    def insert(self, item):
        self.data.append(item)
        i = len(self.data)-1
        while i > 1:
            child=self.data[i]
            parent=self.data[i//2]
            if parent==None:
                break
            elif child>parent:
                self.data[i], self.data[i//2]=parent, child
                i=i//2
            else:
                break;


def solution(x):
    return 0
