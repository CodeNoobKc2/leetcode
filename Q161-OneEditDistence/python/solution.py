class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        pending = ""
        #print(len(t))
        #print(len(s))
        if len(t) == len(s):
            #print('here0')
            for idx,char in enumerate(t):
                if s[idx] == char:
                    pending = pending + char
                else:
                    pending = pending + char + s[idx+1:]
                    return pending == t
            return False

        if len(t) == len(s) - 1:
            #print('here1')
            for idx,char in enumerate(t):
                if s[idx] == char:
                    pending = pending + char
                else:
                    pending = pending + s[idx+1:]
                    return pending == t
            return s[:-1] == t

        if len(t) == len(s) + 1:
            #print('here2')
            for idx,char in enumerate(t[0:-1]):
                if s[idx] == char:
                    pending = pending + char
                else:
                    pending = pending + char + s[idx:]
                    #print(pending)
                    return pending == t
            return s == t[:-1]

        return False
