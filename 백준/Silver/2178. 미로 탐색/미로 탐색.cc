#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAX_DIST 10000

int N, M;
int dy[] = {0, 0, -1, 1};
int dx[] = {-1, 1, 0, 0};

int bfs(vector<vector<int>> &maps, vector<vector<int>> &dist)
{
    queue<pair<int, int>> que;
    que.push({0, 0});
    dist[0][0] = 1;

    while (!que.empty())
    {

        auto [cy, cx] = que.front();
        que.pop();

        for (int d = 0; d < 4; d++)
        {
            int ny, nx;

            ny = cy + dy[d];
            nx = cx + dx[d];

            if (0 <= ny && ny < N && 0 <= nx && nx < M && maps[ny][nx] == 1 && dist[ny][nx] > dist[cy][cx] + 1)
            {
                dist[ny][nx] = dist[cy][cx] + 1;
                que.push({ny, nx});
            }
        }
    }

    return dist[N - 1][M - 1];
}

int main(int argc, char const *argv[])
{
    vector<vector<int>> maps;
    vector<vector<int>> dist;
    cin >> N >> M;

    dist.resize(N, vector<int>(M, MAX_DIST));

    for (int i = 0; i < N; i++)
    {
        string tmp;
        vector<int> tmp_vec = {};
        cin >> tmp;

        for (auto c : tmp)
        {
            tmp_vec.push_back((int)(c - '0'));
        }

        maps.push_back(tmp_vec);
    }

    int shortest_dist = bfs(maps, dist);

    cout << shortest_dist << endl;

    return 0;
}
