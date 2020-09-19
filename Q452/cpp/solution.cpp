#include "algorithm"
#include "iostream"
#include "vector"

using namespace std;

class Solution {
  public:
  int findMinArrowShots(vector<vector<int>>& points)
  {
    int tot = points.size();
    if (tot == 0) {
      return 0;
    }

    if (tot == 1) {
      return 1;
    }

    sort(points.begin(), points.end(), [](vector<int> a, vector<int> b) {
      return a[0] < b[0];
    });

#ifdef DEBUG_OUTPUT
    cout << "points";
    for (int i = 0; i < tot; i++) {
      cout << points[i][0] << ":" << points[i][1] << " ";
    };
    cout << endl;
#endif
    int left = points[0][0];
    int right = points[0][1];
    int arrow = 1;
    vector<int>* balloon = &points[0];

    for (int i = 1; i < tot; i++) {
      balloon = &points[i];
#ifdef DEBUG_OUTPUT
      cout << "left:" << left << "right:" << right << endl;
#endif

      if ((*balloon)[0] > right) {
        arrow++;
        left = (*balloon)[0];
        right = (*balloon)[1];
        continue;
      }

      left = (*balloon)[0];
      right = (*balloon)[1] < right ? (*balloon)[1] : right;
    }

    return arrow;
  }
};
