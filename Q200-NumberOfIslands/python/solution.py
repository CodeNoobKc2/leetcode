from typing import List,Optional,Tuple

class Equivalence:
    def __init__(self):
        self.d = {}

    def addEq(self,left,right):
        if left in self.d:
            raise Exception("duplciate left val in eq")
        self.d[left] = right

    def getEq(self,t) -> any:
        if t in self.d:
            #print(f'eq cur:{t}')
            return self.getEq(self.d[t])
        else:
            return t

class Solution:
    def __init__(self):
        self.marked = {}
        self.eq = Equivalence()

    def getMarker(self,row:int,col:int) -> Optional[int]:
        key = f'{row}-{col}'
        return self.eq.getEq(self.marked[key]) if key in self.marked else None

    def mark(self,row:int,col:int,m:int):
        key = f'{row}-{col}'
        self.marked[key] = m
        #print(self.marked)


    def getSurroundingMarker(self,row:int,col:int) -> Tuple[Optional[int],Optional[int]]:
        return (
            self.getMarker(row-1,col),
            self.getMarker(row,col-1),
        )

    def numIslands(self, grid: List[List[str]]) -> int:
        islandCnt = 0
        mark = 0
        for row,line in enumerate(grid):
            for col,char in enumerate(line):
                if char == "0":
                    continue

                (up,left) = self.getSurroundingMarker(row,col)
                #print(f'row:{row} col:{col} up:{up} left:{left}')
                if up is None and left is None:
                    mark = mark + 1
                    self.mark(row,col,mark)
                    islandCnt = islandCnt + 1
                elif up is None and left is not None:
                    self.mark(row,col,left)
                elif up is not None and left is None:
                    self.mark(row,col,up)
                elif up == left:
                    self.mark(row,col,up)
                else:
                    mark = mark + 1
                    
                    self.mark(row,col,mark)
                    self.eq.addEq(up,mark)
                    self.eq.addEq(left,mark)
                    islandCnt = islandCnt - 1

        return islandCnt
