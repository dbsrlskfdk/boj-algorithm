#include <iostream>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

vector<int> split(string a, char delim)
{
    vector<int> res = {};

    istringstream iss(a);
    string str_buf;

    while (getline(iss, str_buf, delim))
    {
        res.push_back(stoi(str_buf));
    }

    return res;
}

int main()
{
    string st_time;
    string cur_time;
    vector<int> splitted_st;
    vector<int> splitted_cur;
    vector<int> diff_time = {};

    cin >> cur_time;
    cin >> st_time;

    splitted_st = split(st_time, ':');
    splitted_cur = split(cur_time, ':');

    for (int i = splitted_st.size() - 1; i >= 0; i--)
    {
        if (splitted_st[i] - splitted_cur[i] < 0) // 시간의 차이가 0보다 작으면, 앞에 시간에서 끌어써야함(초 -> 분 -> 시)
        {
            if (i != 0)
            {
                diff_time.push_back(splitted_st[i] - splitted_cur[i] + 60);
            }
            else
            {
                diff_time.push_back(splitted_st[i] - splitted_cur[i] + 24);
            }

            if (i - 1 >= 0)
            {
                splitted_cur[i - 1] += 1;
            }
        }
        else
        {
            diff_time.push_back(splitted_st[i] - splitted_cur[i]);
        }
    }

    for (int i = diff_time.size() - 1; i >= 0; i--)
    {
        string str_time = to_string(diff_time[i]);
        str_time.insert(str_time.begin(), 2 - str_time.length(), '0');
        if (i != 0)
        {
            cout << str_time << ':';
        }
        else
        {
            cout << str_time << endl;
        }
    }

    return 0;
}