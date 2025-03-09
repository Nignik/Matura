#include <bits/stdc++.h>

using namespace std;

string f(int k, int n, string s) {
    string t;
    int rows = n / k;
    int step = k;
    int last = 0;
    for (int i = 0; i < k; i++) {
        for (int j = last; j < n && j >= 0; j+=step) {
            t += s[j];
            last = j+1;
        }
        step *= -1;
    }

    return t;
}

int main() {
    cout << f(4, 40, "NKI_ATE_USGACYOKZZ_YYSJTCWEKI_SAEMTRLE_P") << '\n';
}