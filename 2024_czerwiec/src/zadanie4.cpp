#include <bits/stdc++.h>

using namespace std;

void solve2(vector<int>& next) {
    set<int> pcs;
    int i = 1;
    std::generate_n(std::inserter(pcs, pcs.begin()), next.size()-1, [&i](){ return i++; });

    for (auto& nxt : next) {
        pcs.erase(nxt);
    }

    cout << pcs.size() << endl;
}

void solve3(vector<int>& next) {
    // indeksujemy sie od 1
    // next[0] jest nie istotne
    int n = next.size(); // wielkosc naszego vectora

    // tworzymy nowy vector który bedzie przechowywał aktualną pozycje naszych pakietów
    vector<int> packets(n);

    // przypisujemy początkowe pozycje naszych pakietów
    for (int i = 0; i < n; i++) {
        packets[i] = i;
    }

    // iota(packets.begin(), packets.end(), 0); : to jest alternatywna werjsa powyższej petli

    // vector w którym: ans[0] - numer rundy, ans[1] - numer pakietu, ans[2] - czy pojawil sie taki pakiet
    vector<int> ans = {-1, -1, 0};

    // iterujemy sie 10^4 razy, po tylu rundach napewno jakis pakiet sie wroci
    for (int i = 0; i < 1e4; i++) {
        for (int j = 1; j < n; j++) {
            // j-ty pakiet teraz z pozycji packets[j] przesunie sie na pozycje next[packets[j]]
            // To jest ta najciezsza czesc zeby sobie wyobrazic
            packets[j] = next[packets[j]];
        }

        for (int j = 1; j < n; j++) {
            // Sprawdzamy po kolei kazdy pakiet jeżeli j-ty pakiet jest na j-tej pozycji to wrocil sie on
            // Oznacza to że runa jest i+1 a pakiet ktory sie wrocil to j-ty pakiet, ans[2] ustawiamy na 1 zeby ozanczayc ze znalezlismy pakiet
            if (packets[j] == j) {
                ans = {i+1, j, 1};
                break;
            }
        }

        // Tutaj wykorzystujemy ans[2] zeby skonczyc petle i
        if (ans[2] != 0) {
            break;
        }
    }

    cout << ans[0] << ' ' << ans[1] << endl;
}

void solve4(vector<int>& next) {
    vector<int> mx(8);
    vector<int> cnt(next.size(), 1);

    for (int i = 0; i < 8; i++) {
        vector<int> new_cnt(next.size());
        for (int j = 1; j < next.size(); j++) {
            new_cnt[next[j]] += cnt[j];
        }

        for (int j = 1; j < next.size(); j++) {
            mx[i] = max(mx[i], new_cnt[j]);
        }

        cnt = new_cnt;
    }

    for (int i = 1; i <= 8; i*=2) {
        cout << mx[i-1] << ' ';
    }
    cout << endl;
}

int main() {
    ifstream f("../dane/odbiorcy.txt");

    vector<int> next = {-1};

    int x;
    while (f >> x) {
        next.push_back(x);
    }

    solve2(next);
    solve3(next);
    solve4(next);
    
}