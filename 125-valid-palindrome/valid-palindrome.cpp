#include <string>
#include <algorithm>

class Solution {
public:
    bool isPalindrome(string s) {
   
        string filtered;
        for (char c : s) {
            if (std::isalnum(c)) {
                filtered += std::tolower(c);
            }
        }
        int start = 0;
        int end = filtered.length() - 1;
        
        return helper(filtered, start, end);
    }

private:
    bool helper(const std::string& s, int start, int end) {
        while (start < end) {
            if (s[start] != s[end]) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
};
