#include <iostream>
#include <vector>

using namespace std;

long long int fibo(int n)
{
    vector<long long int> fibo_vec = {0, 1};

    for (int i = 2; i <= n; i++)
    {
        fibo_vec.push_back(fibo_vec[i - 1] + fibo_vec[i - 2]);
    }
    return fibo_vec.at(n);
}

int main(int argc, char const *argv[])
{
    int n;

    cin >> n;
    cout << fibo(n) << endl;
    return 0;
}
