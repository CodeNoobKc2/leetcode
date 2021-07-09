# Solution
## Moorve voting
### Assumption
1. Major number does exist
### Proof
Given list length is Tot
Given major as Nmajor and arbitrary number as N0 and this number cannot be Major
Given potential candidates which cannot be Nmajor or N0 as set P

Suppose the last candidate is N0 and last
If Cnt(Tot) == 0, which means no major number exists, conflict with Assumption 1
If Cnt(Tot) > 0, which means N0 has not meet enough opponent during the whole voting process.
However, by Assumption we can conclude that Freq(Major) > Freq(N0) + Freq(P), which means Freq(Major) - Freq(P) > Freq(N0).
Thus during the whole voting process, the times N0 meet Major must be greater than Freq(N0).
Thus Cnt(Tot) cannot be greator than zero.
So the last candidate cannot be N0 while N0 doesnot equal to Major
