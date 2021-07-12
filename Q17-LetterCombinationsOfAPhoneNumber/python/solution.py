from typing import Dict,List

numberToLetters:Dict[str,str] = {
    "2":"abc",
    "3":"def",
    "4":"ghi",
    "5":"jkl",
    "6":"mno",
    "7":"pqrs",
    "8":"tuv",
    "9":"wxyz"
}

class Solution:
    def recursiveGeneration(self, current:str,restNumbers:str,answer:List[str]):
        if len(restNumbers) == 0:
            answer.append(current)
            return
        for char in numberToLetters[restNumbers[0]]:
            self.recursiveGeneration(current+char,restNumbers[1:],answer)

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        answer:List[str] = []
        self.recursiveGeneration("",digits,answer)
        return answer
