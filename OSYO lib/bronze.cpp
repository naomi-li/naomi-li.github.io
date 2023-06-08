#include <bits/stdc++.h>
using namespace std;

string all_dices[4];
int N;


int match(string dices[], char letter) {
    for (int y = 0; y < 4; y++) {
        for (int z = 0; z < 6; z++) {
            if (dices[y][z] == letter) {
                return y;
            }
        }
    }
    return -1;
}



int main() {
    

    cin >> N;

    for (int i = 0; i < 4; i++) {
        cin >> all_dices[i];
    }

    while (N--) {

        string dices[4];
        dices[0] = all_dices[0];
        dices[1] = all_dices[1];
        dices[2] = all_dices[2];
        dices[3] = all_dices[3];


        string word;
        cin >> word;

        int count = 0;

        for (int x = 0; x < word.size(); x++) {
            int temp = match(dices, word[x]);
            if (temp < 0) {
                cout << "NO" << endl;
                break;
            }
            else {
                count++;
                dices[temp] = "";
            }
        }

        if (count == word.size()) cout << "YES" << endl;

    }
}