#include "./solution.cpp"
#include <iostream>

using namespace std;

int main()
{
  auto solution = new Solutions();
  vector<int> test = vector<int>({ -1, 0, 1, 2, -1, -4 });
  solution->threeSum(test);
  vector<int> test2 = vector<int>({ 0, 0, 0 });
  solution->threeSum(test2);
  vector<int> test3 = vector<int>({ -1, 0, 1 });
  solution->threeSum(test3);
  vector<int> test4 = vector<int>({ 0, 0, 0, 0 });
  solution->threeSum(test4);
  vector<int> test5 = vector<int>({ -2, 0, 1, 1, 2 });
  solution->threeSum(test5);
  vector<int> test6 = vector<int>({ -4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6 });
  solution->threeSum(test6);
  return 0;
}
