#include <string>
#include <vector>

using namespace std;
int res = 9;
void dp(int N, int number, int cnt, int now)
{
    if (cnt > 8)
        return;
    if (number == now)
    {
        res = min(res, cnt);
        return;
    }
    int op = 0;
    for (int i = 1; i <= 9; i++)
    {
        op = op * 10 + N;
        dp(N, number, cnt + i, now + op);
        dp(N, number, cnt + i, now - op);
        if (now != 0)
        {
            dp(N, number, cnt + i, now * op);
            dp(N, number, cnt + i, now / op);
        }
    }
}
int solution(int N, int number) {
    int answer = 0;
    dp(N, number, 0, 0);
    if (res > 8)
        answer = -1;
    else
        answer = res;
    return answer;
}