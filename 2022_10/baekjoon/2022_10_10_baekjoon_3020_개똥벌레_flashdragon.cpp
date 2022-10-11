#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
int top[100001];
int bot[100001];
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	int n, h;
	cin >> n >> h;
	for (int i = 0; i < n; i++)
	{
		if (i % 2 == 0)
		{
			cin >> bot[i / 2];
		}
		else
		{
			cin >> top[i / 2];
		}
	}
	sort(top, top + n / 2);
	sort(bot, bot + n / 2);
	int answer = 200000;
	int cnt = 0;
	for (int i = 1; i <= h; i++)
	{
		int temp1 = lower_bound(bot, bot + n / 2, i) - bot;
		int temp2 = upper_bound(top, top + n / 2, h - i) - top;
		int temp = (n / 2 - temp1) + (n / 2 - temp2);
		if (temp < answer)
		{
			answer = temp;
			cnt = 1;
		}
		else if (temp == answer)
			cnt++;
	}
	cout << answer << " " << cnt;
}