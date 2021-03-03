#define DEBUG_OUTPUT
#include "solution.cpp"
#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main()
{
  auto solution = new Solution();
  vector<int> case0_arr = { -1, 2, 1, -4 };
  int case0_target = 1;
  solution->threeSumCloset(case0_arr, case0_target);
  cout << endl
       << "-------------------------------" << endl;
  vector<int> case1_arr = { 1, 1, 1, 0 };
  int case1_target
      = 100;
  solution->threeSumCloset(case1_arr, case1_target);
  cout << endl
       << "-------------------------------" << endl;
  vector<int> case2_arr = { 1, 1, 1, 1 };
  int case2_target = 3;
  solution->threeSumCloset(case2_arr, case2_target);
}
