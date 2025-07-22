#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution{
    public:
    int coin_change(vector<int>& coins, int amount){
        sort(coins.begin(), coins.end());

        int n = coins.size();
        vector<int> dp(amount+1, amount+1);
        dp[0] = 0;

        for (int i=1; i<amount+1; i++){
            for(int coin: coins){
                
                if (coin > i) break;

                dp[i] = min(
                    dp[i-coin]+1,
                    dp[i]
                );
            }
        }
        if (dp[amount] == amount+1) return -1;
        else return dp[amount];
    }
};


int main(){
    Solution solution;
    vector<int> coins = {474,83,404,3};
    int amount = 264;
    cout << solution.coin_change(coins, amount);
    return 0;
}