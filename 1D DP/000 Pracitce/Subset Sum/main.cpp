#include <iostream>
#include <vector>

using namespace std;

class Solution{
    public:
    bool subsetsum(const vector<int>& arr, int target){
        int n = arr.size();
        vector<int> dp(target+1);
        dp[0] = 1;

        for (int i=0; i<n; i++){
            for (int j=target; j>=arr[i]; j--){
                int num = arr[i];
                dp[j] = dp[j-num] || dp[j];
            }

            if (dp[target]) return true;
        }
        return dp[target]; 
    }
};

int main(){
    
    Solution solution;

    vector<int> arr = {3, 34, 4, 12, 5, 2};
    int sum = 9;

    cout << solution.subsetsum(arr, sum);
    return 0;
}