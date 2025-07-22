#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Solution{
    public:

    int cutrod(vector<int>& prices){
        int n = prices.size();
        vector<int> dp(n+1);

        for (int i=1; i<n+1; i++){
            int price = prices[i-1];
            for (int j=i; j< n+1; j++){
                dp[j] = max(
                    dp[j-i] + price,
                    dp[j]
                );
            }
        }

        auto max_it = max_element(dp.begin(), dp.end());

        int max_value = *max_it;
        return max_value;
    }
};

int main(){

    Solution solution;
    vector<int> prices = {1, 5, 8, 9, 10, 17, 17, 20};
    cout << solution.cutrod(
        prices=prices
    );
    return 0;
}