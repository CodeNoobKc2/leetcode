questionMark = "?"
colon = ":"

class Solution:
    def recursive(self,offset:int,expression:str) -> str:
        if expression[offset] == "F":
            questionMarkCnt = 0
            offset = offset + 2
            while offset < len(expression):
                #print(f'ommit_left_offset {offset} currentChar {expression[offset]}')
                nextChar = expression[offset+1]
                if nextChar == colon and questionMarkCnt == 0:
                    #print(f'break_left_offset {offset} currentChar {expression[offset]}')
                    break;
                if nextChar == colon and questionMarkCnt !=0:
                    questionMarkCnt = questionMarkCnt - 1
                if nextChar == questionMark:
                    questionMarkCnt = questionMarkCnt + 1
                offset = offset + 2
                
            if offset + 3 >= len(expression):
                return expression[-1]
            
            if expression[offset + 3] == colon:
                #print(expression[offset:offset+3])
                return expression[offset + 2]

            offset = offset + 2
            return self.recursive(offset,expression)
        else:
            
            if expression[offset+3] is colon:
                
                return expression[offset+2]
            
            return self.recursive(offset+2,expression)
        
    def parseTernary(self, expression: str) -> str:
        return self.recursive(0,expression)
