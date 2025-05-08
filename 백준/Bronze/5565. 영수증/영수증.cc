#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
    int total_price;
    int cum_price = 0;

    cin >> total_price;

    int temp_price;
    for (int i = 0; i < 9; i++)
    {
        cin >> temp_price;
        cum_price += temp_price;
    }

    cout << total_price - cum_price << endl;
    return 0;
}
