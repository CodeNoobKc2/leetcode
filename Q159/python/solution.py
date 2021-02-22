from typing import List

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 0:
            return 0

        k = 2
        maxLen = 1

        elements:List[set] = [None] * k
        lens:List[int] = [1] * k

        elements[0] = set(s[0],)

        for idx,char in enumerate(s[1:]):
            #print(char+'-'*10,s[idx])

            if char == s[idx]:
                last = 0
                for j in range(k):
                    if elements[j] is None:
                        last = j - 1
                        break

                    last = j
                    lens[j] = lens[j] + 1

                maxLen = maxLen if maxLen > lens[last] else lens[last]
                continue

            newElements:List[set] = [None] * k
            newLens:List[int] = [1] * k
            newElements[0] = set((char,))

            last = 0
            for i in range(k):
                if elements[i] is None:
                    break

                last = i

                if char in elements[i]:
                    newElements[i] = elements[i].copy()
                    newLens[i] = lens[i] + 1
                    last = i
                else:
                    if not i+1 is k:
                        last = i + 1
                        newset = elements[i].copy()
                        newset.add(char)

                        newElements[i+1] = newset
                        newLens[i+1] = lens[i] + 1

            #for idx,elms in enumerate([x for x in newElements if x is not None]):
            #    print(f'sets {elms} len {newLens[idx]} ')

            elements = newElements
            lens = newLens
            #print(last)
            maxLen = maxLen if maxLen > lens[last] else lens[last]

        return maxLen
        
if __name__ == "__main__":
    solution = Solution()

    testcases = [
        {"input":"eceba","output":3},
        {"input":"ccaabbb","output":5},
    ]

    for idx,testcase in enumerate(testcases):
        print(f'testcase {idx} start. input {testcase["input"]}')
        computed = solution.lengthOfLongestSubstringTwoDistinct(testcase["input"])
        if computed != testcase["output"]:
            print(f'testcase {idx} failed expected {testcase["output"]} get {computed}.')
            exit(1)
        print(f'testcase {idx} pass.')
