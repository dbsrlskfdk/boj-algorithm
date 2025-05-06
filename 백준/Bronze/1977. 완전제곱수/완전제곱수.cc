#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main(int argc, char const *argv[])
{
    int M;
    int N;
    int sum_vec = 0;
    int min_perfectSquare = 10000;
    vector<int> perfectSqures;

    cin >> M;
    cin >> N;

    for (int i = M; i <= N; i++)
    {
        int sqrt_i = sqrt(i);
        if (sqrt_i * sqrt_i == i)
        {
            perfectSqures.push_back(i);
            if (min_perfectSquare > i)
            {
                min_perfectSquare = i;
            }
        }
    }

    if (perfectSqures.empty())
    {
        cout << -1 << endl;
    }
    else
    {
        for (int i = 0; i < perfectSqures.size(); i++)
        {
            sum_vec += perfectSqures.at(i);
        }
        cout << sum_vec << endl;
        cout << min_perfectSquare << endl;
    }

    return 0;
}
