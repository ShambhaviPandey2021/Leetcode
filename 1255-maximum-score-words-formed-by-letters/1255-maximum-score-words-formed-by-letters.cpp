
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxScoreWords(vector<string>& words, vector<char>& letters, vector<int>& score) {
    
        unordered_map<char, int> letters_count;
        for (char letter : letters) {
            letters_count[letter]++;
        }
        
        return backtrack(words, score, letters_count, 0);
    }

private:
 
    int wordScore(const string& word, const vector<int>& score) {
        int total_score = 0;
        for (char c : word) {
            total_score += score[c - 'a'];
        }
        return total_score;
    }

  
    bool canForm(const string& word, unordered_map<char, int>& letters_count) {
        unordered_map<char, int> word_count;
        for (char c : word) {
            word_count[c]++;
            if (word_count[c] > letters_count[c]) {
                return false;
            }
        }
        return true;
    }

    int backtrack(vector<string>& words, const vector<int>& score, unordered_map<char, int>& letters_count, int index) {
        if (index == words.size()) {
            return 0;
        }

        int max_score = backtrack(words, score, letters_count, index + 1);

        string word = words[index];
        if (canForm(word, letters_count)) {
        
            for (char c : word) {
                letters_count[c]--;
            }
            max_score = max(max_score, wordScore(word, score) + backtrack(words, score, letters_count, index + 1));

         
            for (char c : word) {
                letters_count[c]++;
            }
        }

        return max_score;
    }
};
