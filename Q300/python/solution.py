from typing import List,Optional,Tuple
import logging, sys

class HeapNode:

    def __init__(self,val:int,lenMax:int = 1):
        self.val = val
        self.lenMax = 1
        self.rightNode:Optional[HeapNode] = None
        self.leftNode:Optional[HeapNode] = None

class OrderedGreaterHeap:
    def __init__(self):
        self.top:Optional[HeapNode] = None

    def debugPrint(self):
        level:int = -1
        queue:List[HeapNode] = [self.top]
        
        while not len(queue) is 0:
            current = queue.pop(0)

            if len(queue) is 0:
                level = level + 1

            nodeId = hex(id(current))
            print(f'level {level} id {nodeId} val {current.val} lenMax {current.lenMax}')

            if current.leftNode != None:
                print(f'id {nodeId} leftNode {hex(id(current.leftNode))}')
                queue.append(current.leftNode)

            if current.rightNode != None:
                print(f'id {nodeId} rightNode {hex(id(current.rightNode))}')
                queue.append(current.rightNode)


        print('complete'+'-'*20)


    def justSmallerRecursive(self,val,top)->HeapNode:
        if top.val < val :
            return top

        return None

    def justSmaller(self,val:int)->HeapNode:
        return self.justSmallerRecursive(val,self.top)


    def push(self,val,lenMax:int):
        if self.top is None:
            self.top = HeapNode(val,lenMax)
            return

        if val > self.top.val :
            newTop = HeapNode(val,lenMax)
            newTop.leftNode = self.top
            self.top = newTop
            return

        if val <= self.top.val :
            newNode = HeapNode(val,lenMax)

            parent = self.top
            rchild = self.top.rightNode
            while not rchild is None:
                if val > rchild.val:
                    break
                parent = rchild
                rchild = rchild.rightNode

            newNode.leftNode = rchild
            parent.rightNode = newNode
            return

        #if val == self.top.val :
        #    newNode = HeapNode(val)
        #    newNode.lenMax = self.top.lenMax
        #    newNode.leftNode = self.top.rightNode
        #    self.top.rightNode = newNode
        #    return newNode


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        heap = OrderedGreaterHeap()

        lenMax = 0

        for idx,num in enumerate(nums):
            print(nums[0:idx+1])
            (node,parent) = heap.push(num)
            nodeIter = node.leftNode

            nodeLenMax = node.lenMax
            while not nodeIter is None:
                nodeLenMax = nodeLenMax if nodeLenMax > 1 + nodeIter.lenMax else  1 + nodeIter.lenMax
                nodeIter = nodeIter.rightNode

            if not parent is None:
                #print(num,parent.val)
                sibling = parent.leftNode
                while not sibling is None and sibling.val >= num:
                    sibling = sibling.rightNode

                while not sibling is None:
                    #print(sibling.val,sibling.lenMax)
                    nodeLenMax = max([nodeLenMax,sibling.lenMax + 1])
                    sibling = sibling.rightNode

            node.lenMax = nodeLenMax

            heap.debugPrint()

            lenMax = lenMax if lenMax > nodeLenMax else nodeLenMax

        return lenMax


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("start testing")
    solution = Solution()

    tCase="input"
    tResult="output"
    testCases=[
        {tCase:[10,9,2,5,3,7,101,18],tResult:4},
        {tCase:[0,1,0,3,2,3],tResult:4},
        {tCase:[7,7,7,7,7,7,7],tResult:1},
        {tCase:[4,10,4,3,8,9],tResult:3},
        {tCase:[5,7,-24,12,13,2,3,12,5,6,35],tResult:6},
    ]

    idx=0
    for testCase in testCases:
        caculated = solution.lengthOfLIS(testCase[tCase])
        if caculated != testCase[tResult]:
            print("Testcase: {} failed. Expected: {}, Caculated: {}".format(idx,testCase[tResult],caculated))
            exit(1)
        idx=idx+1
        print("Testcase: {} passed.".format(idx))
        print("-"*20)
