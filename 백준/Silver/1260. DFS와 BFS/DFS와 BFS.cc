#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

#define N_MAX 1000
#define M_MAX 10000

int N, M, V;

vector<int> graphs[N_MAX + 1] = {};

bool visited_dfs[N_MAX + 1] = {false};
bool visited_bfs[N_MAX + 1] = {false};

void dfs(int st_v)
{
    visited_dfs[st_v] = true;

    cout << st_v << " ";
    for (int next_v : graphs[st_v])
    {
        if (!visited_dfs[next_v])
        {
            dfs(next_v);
        }
    }
}

void bfs(int st_v)
{
    queue<int> q;
    q.push(st_v);
    visited_bfs[st_v] = true;

    cout << st_v << " ";

    while (!q.empty())
    {
        int cur_v = q.front();
        q.pop();

        for (int next_v : graphs[cur_v])
        {
            if (!visited_bfs[next_v])
            {
                visited_bfs[next_v] = true;
                q.push(next_v);
                cout << next_v << " ";
            }
        }
    }
    cout << endl;
}

int main(int argc, char const *argv[])
{
    cin >> N >> M >> V;

    for (int m = 0; m < M; m++)
    {
        int v1, v2;
        cin >> v1 >> v2;
        graphs[v1].push_back(v2);
        graphs[v2].push_back(v1);
    }

    for (int i = 1; i <= N_MAX; i++)
    {
        sort(graphs[i].begin(), graphs[i].end());
    }

    dfs(V);
    cout << endl;
    bfs(V);
    return 0;
}
