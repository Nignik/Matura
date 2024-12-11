#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void solve1(vector<string> words) {
    string sample = "k?t";

    int ans = 0;
    for (int i = 0; i < words.size(); i++) {
        for (int l = 0, r = 2; r < words[i].size(); l++, r++) {
            vector<char> x;
            for (int j = l; j <= r; j++) {
                x.push_back(words[i][j]);
            }

            if (x[0] == 'k' && x[2] == 't') {
                ans++;
                break;
            }
        }
    }

    cout << ans << endl;
}

void solve2(vector<string> words) {
    vector<string> encoded_words = words;
    for (auto& word : encoded_words) {
        for (auto& letter : word) {
            letter = ((letter - 97) + 13) % 26 + 97;
        }
    }

    int ans = 0;
    string best_word;
    for (int i = 0; i < words.size(); i++) {
        reverse(words[i].begin(), words[i].end());
        if (words[i] == encoded_words[i]) {
            ans++;
            best_word = best_word.size() >= encoded_words[i].size() ? best_word : encoded_words[i];
        }
    }

    cout << ans << endl;
    reverse(best_word.begin(), best_word.end());
    cout << best_word << endl;
}

void solve3(vector<string> words) {
    vector<string> ans;
    
    for (auto& word : words) {
        vector<int> cnt(26);

        for (auto& letter : word) {
            cnt[letter - 97]++;
        }

        for (auto& x : cnt) {
            if (x >= (word.size() + 1)/2) {
                ans.push_back(word);
                break;
            }
        }
    }

    for (auto& word : ans) {
        cout << word << endl;
    }
}

int main() {
    ifstream f("../dane/slowa.txt");

    vector<string> words;
    string line;
    while (getline(f, line)) {
        words.push_back(line);
    }

    solve3(words);
}