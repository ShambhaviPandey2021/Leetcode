class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> sCount;
        for (char c : s) {
            sCount[c]++;
        }
        string result;
        for (char c : order) {
            if (sCount.find(c) != sCount.end()) {
                int count = sCount[c];
                while (count-- > 0) {
                    result += c;
                }
                sCount.erase(c);
            }
        }      
        for (auto& entry : sCount) {
            int count = entry.second;
            while (count-- > 0) {
                result += entry.first;
            }
        }
        
        return result;
    }
};