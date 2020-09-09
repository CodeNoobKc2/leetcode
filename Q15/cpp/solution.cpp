#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solutions {
  public:
  vector<vector<int>> threeSum(vector<int>& nums)
  {
    if (nums.size() < 3) {
      return {};
    }

    cout << "check for boundry cases" << endl;

    int tot = nums.size();
    cout << "candidates total:" << tot << endl;

    sort(nums.begin(), nums.end());
    int lowestSum = nums[0] + nums[1] + nums[2];
    int hightestSum = nums[tot - 1] + nums[tot - 2] + nums[tot - 3];

    if (lowestSum > 0 || hightestSum < 0) {
      return {};
    }

    cout << "init rtn vector" << endl;
    int nonExistVal = nums[0] - 1;
    int greatestTwoSum = nums[tot - 1] + nums[tot - 2];
    cout << "nonExistVal:" << nonExistVal << "greatestTwoSum:" << greatestTwoSum
         << endl;
    int lowestTwoSum = nums[0] + nums[1];

    int lowerBound = 0;
    int upperBound = tot - 1;

    cout << "shrink upper bound and lower bound" << endl;
    for (; upperBound - lowerBound >= 2;) {
      int lowestTwoSum = nums[lowerBound] + nums[lowerBound + 1];
      int greatestTwoSum = nums[upperBound] + nums[upperBound - 1];

      if (lowestTwoSum + nums[upperBound] > 0) {
        upperBound--;
        continue;
      }

      if (greatestTwoSum + nums[lowerBound] < 0) {
        lowerBound++;
        continue;
      }

      break;
    }

    cout << "lower bound:" << lowerBound << "upper bound:" << upperBound << endl;
    greatestTwoSum = nums[upperBound] + nums[upperBound - 1];

    vector<vector<int>> answer = {};
    int firstElmPos, firstVal, curSum;
    int secondElmPos, secondVal;
    int thirdElmPos, thirdVal;

    for (firstElmPos = lowerBound; firstElmPos <= upperBound - 2;) {
      firstVal = nums[firstElmPos];
      cout << "firstElmPos:" << firstElmPos << "firstVal:" << firstVal << endl;
      if (firstVal > 0) {
        return answer;
      }

      secondElmPos = firstElmPos + 1;
      cout << "secondElmPos:" << secondElmPos << "secondVal:" << nums[secondElmPos] << endl;
      thirdElmPos = upperBound;
      cout << "thirdElmPos:" << thirdElmPos << "thirdVal:" << nums[thirdElmPos] << endl;
      for (; thirdElmPos - secondElmPos >= 1;) {
        secondVal = nums[secondElmPos];
        thirdVal = nums[thirdElmPos];
        curSum = firstVal + secondVal + thirdVal;
        if (curSum > 0) {
          for (; thirdElmPos - secondElmPos >= 1 && nums[thirdElmPos] == thirdVal; thirdElmPos--)
            ;
          cout << "thirdElmPos:" << thirdElmPos << "thirdVal:" << nums[thirdElmPos] << endl;

          continue;
        } else if (curSum < 0) {
          for (; thirdElmPos - secondElmPos >= 1 && nums[secondElmPos] == secondVal; secondElmPos++)
            ;
          cout << "secondElmPos:" << secondElmPos << "secondVal:" << nums[secondElmPos] << endl;

          continue;
        } else {
          cout << "combination:" << firstVal << "," << secondVal << "," << thirdVal << endl;
          answer.push_back({ firstVal, secondVal, thirdVal });
          for (; thirdElmPos - secondElmPos >= 1 && nums[thirdElmPos] == thirdVal; thirdElmPos--)
            ;
          for (; thirdElmPos - secondElmPos >= 1 && nums[secondElmPos] == secondVal; secondElmPos++)
            ;
        }
      }

      // itertate to the next none duplicated value
      for (; upperBound - firstElmPos >= 2 && firstVal == nums[firstElmPos]; firstElmPos++)
        ;
    }
    return answer;
  }
};
