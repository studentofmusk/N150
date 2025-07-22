#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;


class Solution{
    public:
    
    unordered_set<string> codes;
    unordered_map<int, int> memo;
    
    Solution(){
        for (int i=1; i<27; i++){
            codes.insert(to_string(i));
        }
    }

    int dfs(const string& s, int index){

        int n = s.length();

        if (index == n){
            return 1;
        }

        if (memo.count(index)){
            return memo[index];
        }

        int res = 0;

        if (codes.count(s.substr(index, 1))){
            res += dfs(s, index + 1);
        }

        if (index+1 < n && codes.count(s.substr(index, 2))){
            res += dfs(s, index+2);
        }
        memo[index] = res;
        return res;
    }

    int decodeways(string s){
        memo.clear();
        return dfs(s, 0);
    }
};

int main(){
    Solution solution;
    string s = "123";
    cout << solution.decodeways(s);
    return 0;
}