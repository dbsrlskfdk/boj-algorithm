#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[])
{
    int n;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        int p;
        cin >> p;

        int max_price = 0;
        string max_name = "";

        for (int j = 0; j < p; j++)
        {
            int price;
            string name;
            cin >> price >> name;
            if (price > max_price)
            {
                max_price = price;
                max_name = name;
            }
        }

        cout << max_name << endl;
    }

    return 0;
}
