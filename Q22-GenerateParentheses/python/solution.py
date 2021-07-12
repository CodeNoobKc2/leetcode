from typing import List,Set

class Solution:
    def buildParenthesis(self,tot,closed,used:int,cur:str,posible:List[str]):
        if used == tot:
            # close all opened
            for i in range(used-closed):
                cur = cur + ")"
            posible.append(cur)
            return

        self.buildParenthesis(tot,closed,used+1,cur+"(",posible)

        if used-closed > 0:
            self.buildParenthesis(tot,closed+1,used,cur+")",posible)

    def generateParenthesis(self, n: int) -> List[str]:
        posible = []

        self.buildParenthesis(n,0,1,"(",posible)

        return posible

if __name__ == "__main__":
    print(Solution().generateParenthesis(1))
    print(Solution().generateParenthesis(2))
    print(Solution().generateParenthesis(3))
