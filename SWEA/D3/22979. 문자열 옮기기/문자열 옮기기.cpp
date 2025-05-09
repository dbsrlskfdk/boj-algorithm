#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int T;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int K;
        long long int k_buf, total_rotation;
        string S;
        total_rotation = 0;
        cin >> S;
        cin >> K;

        for (int k = 0; k < K; k++)
        {
            cin >> k_buf;
            total_rotation += k_buf;
        }
        int len_S = S.size();
        total_rotation %= len_S;
        if (total_rotation > 0)
        {
            for (int j = 0; j < total_rotation; j++)
            {
                S.push_back(S.front());
                S.erase(0, 1);
            }
        }
        else if (total_rotation < 0)
        {
            total_rotation *= -1;
            for (int j = 0; j < total_rotation; j++)
            {
                S = S.back() + S;
                S.pop_back();
            }
        }
        cout << S << endl;
    }
    return 0;
}
