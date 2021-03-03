#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
  public:
  int threeSumCloset(vector<int>& nums, int target)
  {
    if (nums.size() == 3) {
      return nums[0] + nums[1] + nums[2];
    }

    int tot = nums.size();

#ifdef DEBUG_OUTPUT
    cout << "num size:" << tot << "target:" << target << endl;
#endif
    // sort the nums
    sort(nums.begin(), nums.end());
#ifdef DEBUG_OUTPUT
    cout << "sorted:";
    for (int i = 0; i < tot; i++) {
      cout << nums[i] << ",";
    }
    cout << endl;
#endif

    int smallestGap = 10 * 10 * 10 * 10;
    int smallestSum;

    int candidate;
    int fixedElm, res, indicator;
    int leftCursor, leftVal, rightVal, rightCursor;

    for (int i = 0; i < tot; i++) {
      fixedElm = nums[i];

      leftCursor = i == 0 ? 1 : 0, leftVal = nums[leftCursor];
      rightCursor = i == tot - 1 ? tot - 2 : tot - 1, rightVal = nums[rightCursor];

#ifdef DEBUG_OUTPUT
      cout << "fixedElm:" << fixedElm << endl;
#endif

      for (; leftCursor < rightCursor;) {
        if (leftCursor == i) {
          leftCursor++;
          continue;
        }

        if (rightCursor == i) {
          rightCursor--;
          continue;
        }

        leftVal = nums[leftCursor];
        rightVal = nums[rightCursor];
        candidate = leftVal + rightVal + fixedElm;
        indicator = candidate - target;

#ifdef DEBUG_OUTPUT
        cout << "leftVal:" << leftVal << ","
             << "rightVal:" << rightVal << "curSum:" << indicator << endl;
#endif

        if (indicator == 0) {
          return target;
        }

        if (abs(indicator) < smallestGap) {
          smallestGap = abs(indicator);
          smallestSum = candidate;
        }

        if (indicator > 0) {
          rightCursor--;
          continue;
        } else {
          leftCursor++;
          continue;
        }
      }
    }

#ifdef DEBUG_OUTPUT
    cout << "smallestSum:" << smallestSum << endl;
#endif

    return smallestSum;
  }
};
