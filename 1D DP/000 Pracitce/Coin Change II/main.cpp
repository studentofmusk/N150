#include <iostream>
#include <vector>

using namespace std;

class Solution{
    public:
    int coinchange(const vector<int>& arr, int target){
        int n = arr.size();

        vector<int> dp(target+1);
        dp[0] = 1;

        for (int i=0; i<n; i++){
            for (int j=arr[i]; j < target+1; j++){
                dp[j] = dp[j-arr[i]] + dp[j];
            }
        }

        return dp[target];
    }
};

int main(){

    Solution solution;

    vector<int> coins = {1,2,3};
    int sum = 4;
    cout << solution.coinchange(coins, sum);

    return 0;
}
