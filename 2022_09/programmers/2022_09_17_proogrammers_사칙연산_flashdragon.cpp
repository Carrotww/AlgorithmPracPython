#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
using namespace std;
int updp[102][102];
int downdp[102][102];
vector<char>op;
int solution(vector<string> arr)
{
    int answer = -1;
    for (int i = 0; i < arr.size(); i++)
    {
        if (i % 2 == 0)
        {
            int temp = stoi(arr[i]);
            int index = i / 2;
            updp[index][index] = temp;
            downdp[index][index] = temp;
        }
        else
        {
            op.push_back(arr[i][0]);
        }
    }
    int n = op.size() + 1;
    for (int i = 1; i < n; i++)
    {
        for (int j = 0; j + i < n; j++)
        {
            int utemp;
            int dtemp;
            for (int k = j; k < j + i; k++)
            {
                if (op[k] == '+')
                {
                    if (k == j)
                    {
                        utemp = updp[j][k] + updp[k + 1][j + i];
                        dtemp = downdp[j][k] + downdp[k + 1][j + i];
                    }
                    if (utemp < updp[j][k] + updp[k + 1][j + i])
                        utemp = updp[j][k] + updp[k + 1][j + i];
                    if (dtemp > downdp[j][k] + downdp[k + 1][j + i])
                        dtemp = downdp[j][k] + downdp[k + 1][j + i];
                }
                else
                {
                    if (k == j)
                    {
                        utemp = updp[j][k] - downdp[k + 1][j + i];
                        dtemp = downdp[j][k] - updp[k + 1][j + i];
                    }
                    if (utemp < updp[j][k] - downdp[k + 1][j + i])
                        utemp = updp[j][k] - downdp[k + 1][j + i];
                    if (dtemp > downdp[j][k] - updp[k + 1][j + i])
                        dtemp = downdp[j][k] - updp[k + 1][j + i];
                }
            }
            updp[j][j + i] = utemp;
            downdp[j][j + i] = dtemp;
        }
    }
    answer = updp[0][n - 1];
    return answer;
}