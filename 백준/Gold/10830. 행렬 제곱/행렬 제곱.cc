#include <iostream>
#include <vector>

using namespace std;

int N;
long long B;
vector<vector<int>> matrix;

vector<vector<int>> power_of_matrix(vector<vector<int>> &A, long long pow)
{
    vector<vector<int>> half_A;
    vector<vector<int>> sum_matrix;
    sum_matrix.resize(N, vector<int>(N, 0));

    if (pow == 1) // 제곱할 계수가 1이면, 그냥 원본 반환
    {
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                A[i][j] = A[i][j] % 1000;
            }
        }
        return A;
    }
    else if ((pow % 2) == 0) // 제곱할 계수가 짝수이면, A^(pow/2) * A^(pow/2) 로 계산
    {
        vector<vector<int>> half_A = power_of_matrix(A, pow / 2);
        for (int i = 0; i < N; i++) // i 행
        {
            for (int j = 0; j < N; j++) // j 열
            {
                int temp_sum = 0;
                for (int n = 0; n < N; n++)
                {
                    temp_sum += half_A[i][n] * half_A[n][j];
                }
                sum_matrix[i][j] = temp_sum % 1000;
            }
        }
    }
    else if ((pow % 2) == 1) // 제곱할 계수가 홀수이면, A^(⌊pow/2⌋) * A^(⌊pow/2⌋) * A 로 계산
    {
        vector<vector<int>> half_A = power_of_matrix(A, pow / 2);
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                int temp_sum = 0;
                for (int n = 0; n < N; n++)
                {
                    temp_sum += half_A[i][n] * half_A[n][j];
                }
                sum_matrix[i][j] = temp_sum % 1000; // 앞에 원소를 업데이트 하면서, 행렬의 계산을 진행하면 틀린 결과가 나옴. -> [8, 0, 8] [[1], [0], [1]] 업데이트 과정을 생각해보면, [16, 0, 8] -> [16, 0, 8] -> [16, 0, 24] 이렇게 뒤 원소에서는 연산에 필요한 앞 원소를 수정해버려서 문제가 생김.
            }
        }

        for (int i = 0; i < N; i++)
        {
            vector<int> temp_row;
            temp_row.resize(N, 0);

            for (int j = 0; j < N; j++)
            {
                int temp_sum = 0;
                for (int n = 0; n < N; n++)
                {
                    temp_sum += sum_matrix[i][n] * A[n][j];
                }
                temp_row[j] = temp_sum % 1000;
            }

            for (int j = 0; j < N; j++)
            {
                sum_matrix[i][j] = temp_row[j];
            }
        }
    }

    return sum_matrix;
}

int main(int argc, char const *argv[])
{
    cin >> N >> B;

    matrix.resize(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cin >> matrix[i][j];
        }
    }

    // Power 계수가 짝수면, 절반으로 나눠서 계산 반복  ex) A^8 = A^4 * A^4 = (A^2 * A^2) * (A^2 * A^2)
    // Power 계수가 홀수면, 절반으로 나눈 것 2개 + 1로 시작 ex) A^9 = A^4 * A^4 * A = (A^2 * A^2) * (A^2 * A^2) * A

    vector<vector<int>> result;
    result.resize(N, vector<int>(N, 0));

    result = power_of_matrix(matrix, B);

    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            cout << result[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;
}
