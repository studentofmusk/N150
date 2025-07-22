#include <iostream>
#include <vector>

using namespace std;

class Solution{
    public:
        int nth_fib(int n){
            if (n <=1) return n;

            vector<int> dp(n+1);
            dp[0] = 0;
            dp[1] = 1;

            for (int i=2; i<n+1; i++){
                dp[i] = dp[i-1] + dp[i-2];
            }

            return dp[n];
        }
};


int main(){
    Solution solution;
    cout << solution.nth_fib(6); 

    return 0;
}