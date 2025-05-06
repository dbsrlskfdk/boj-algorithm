#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>

using namespace std;

bool compare(tuple<int, int, int, string> &a, tuple<int, int, int, string> &b);

int main(int argc, char const *argv[])
{
    int n;
    vector<tuple<int, int, int, string>> birthdays;

    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string name;
        int day;
        int month;
        int year;

        cin >> name >> day >> month >> year;

        birthdays.push_back(make_tuple(year, month, day, name));
    }

    sort(birthdays.begin(), birthdays.end(), compare);

    cout << get<3>(birthdays.back()) << endl;
    cout << get<3>(birthdays.front()) << endl;
    return 0;
}

bool compare(tuple<int, int, int, string> &a, tuple<int, int, int, string> &b)
{
    if (get<0>(a) == get<0>(b))
    {
        if (get<1>(a) == get<1>(b))
        {
            return get<2>(a) < get<2>(b);
        }
        return get<1>(a) < get<1>(b);
    }
    return get<0>(a) < get<0>(b);
}
