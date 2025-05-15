#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;

vector<vector<int>> maps = {};
vector<vector<bool>> visited;
int dy[] = {0, 0, -1, 1};
int dx[] = {-1, 1, 0, 0};

int main()
{
    int num = 0;
    int max_area = 0;

    cin >> N >> M;

    maps.resize(N, vector<int>(M));
    visited.resize(N, vector<bool>(M, false));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> maps[i][j];
        }
    }

    /*
    Outputs:
    - int num: 그림의 갯수
    - int max_area: 가장 넓은 그림의 넓이
    */
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            if (maps[i][j] == 1 && !visited[i][j]) // 도화지에 그림(1)이면, 탐색시작
            {
                num += 1;
                int tmp_area = 1;
                queue<pair<int, int>> que;
                que.push(make_pair(i, j));
                visited[i][j] = true;

                while (!que.empty())
                {
                    auto front = que.front();
                    auto [cy, cx] = front;
                    que.pop();

                    for (int d = 0; d < 4; d++)
                    {
                        int ny = cy + dy[d];
                        int nx = cx + dx[d];

                        if (((0 <= ny) && (ny < N)) && ((0 <= nx) && (nx < M)) && maps[ny][nx] == 1 && !visited[ny][nx])
                        {
                            que.push(make_pair(ny, nx));
                            visited[ny][nx] = true;
                            tmp_area += 1;
                        }
                    }
                }

                if (max_area < tmp_area)
                {
                    max_area = tmp_area;
                }
            }
        }
    }

    cout << num << endl
         << max_area;
}
