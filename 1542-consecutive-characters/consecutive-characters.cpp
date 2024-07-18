class Solution {
public:

    int maxPower(string s) {
        if (s.empty()) return 0; 
        int maxCount = 1;
        int count = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s[i] == s[i - 1]) {
                count++;
            } else {
                maxCount = max(maxCount, count);
                count = 1; 
            }
        }

        maxCount = max(maxCount, count);

        return maxCount;
    }
};