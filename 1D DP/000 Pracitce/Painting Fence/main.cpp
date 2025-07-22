#include <iostream>
#include <vector>

using namespace std;

class Solution{
public:
    int countWays(int n, int k){
        vector<int> dp(n+1);
        dp[1] = k;
        dp[2] = k * k;

        for (int i=3; i < n+1; i++){
            dp[i] = (dp[i-1] + dp[i-2])*(k-1);
        }
        return dp[n];

    }
};

int main(){
    Solution solution;

    cout << solution.countWays(3, 2);
    return 0;
}