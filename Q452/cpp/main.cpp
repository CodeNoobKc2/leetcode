#define DEBUG_OUTPUT
#include "solution.cpp"
#include <iostream>
using namespace std;

struct testCase {
  vector<vector<int>> points;
  int arrows;
};

int main()
{
  auto solution = Solution();

  vector<testCase> cases = {
    { { { 10, 16 }, { 2, 8 }, { 1, 6 }, { 7, 12 } }, 2 }
  };

  for (int i = 0; i < cases.size(); i++) {
    cout << "test case:" << i << endl;
    auto tc = cases[i];
    int caculated = solution.findMinArrowShots(tc.points);
    cout << "expected:" << tc.arrows << "caculated:" << caculated << endl;
    cout << "---------test finish----------------------" << endl;
  };
  return 0;
}
