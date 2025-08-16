#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution{
    public:
    int subSumOfK(const vector<int>& arr, int k){
        int n = arr.size();
        int res = 0;
        for (int i=0; i < n-k+1; i++){
            int Min = arr[i];
            int Max = arr[i];
            for(int j=i; j < i+k; j++){
                Min = min(Min, arr[j]);
                Max = max(Max, arr[j]);
            }
            res += (Min + Max);
        }
        return res;
    }
};

int main(){
    Solution solution;
    vector<int> arr = {2, 5, -1, 7, -3, -1, -2};
    int k = 4;
    cout << solution.subSumOfK(arr, k);
    return 0;
}