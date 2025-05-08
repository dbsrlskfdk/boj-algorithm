#include <iostream>
#include <cmath>

using namespace std;

int gcd(int a, int b)
{

    int remainder = a % b;
    a = b;
    b = remainder;

    while (b != 0)
    {
        remainder = a % b;

        a = b;
        b = remainder;
    }

    return a;
}

int lcm(int a, int b)
{
    int lowest_common_multiple = a * b / gcd(a, b);

    return lowest_common_multiple;
}

int main(int argc, char const *argv[])
{
    int a, b;

    cin >> a >> b;

    cout << gcd(a, b) << endl
         << lcm(a, b) << endl;
    return 0;
}
