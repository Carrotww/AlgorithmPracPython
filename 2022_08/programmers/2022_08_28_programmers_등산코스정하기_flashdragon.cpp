#include<iostream>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<set>
#include<queue>
#include<map>
using namespace std;
typedef long long ll;
struct go {
	int b, w;
	bool operator<(const go& temp)const {
		if (w == temp.w)
			return b > temp.b;
		return w > temp.w;
	}
};
vector<go> vt[50001];
int kind[500001] = { 0 };
bool vist[500001] = { 0 };
vector<int> solution(int n, vector<vector<int>> paths, vector<int> gates, vector<int> summits) {
	vector<int> answer;
	priority_queue<go>q;
	for (auto i : gates)
	{
		kind[i] = 1;
	}
	for (auto i : summits)
	{
		kind[i] = 2;
	}
	for (auto i : paths)
	{
		int a = i[0];
		int b = i[1];
		int w = i[2];
		vt[a].push_back({ b,w });
		vt[b].push_back({ a,w });
	}
	int res = 10000001;
	int top = -1;
	for (auto st : gates)
	{
		memset(vist, 0, sizeof(vist));
		vist[st] = 1;
		int dis = 0;
		for (int i = 0; i < vt[st].size(); i++)
		{
			q.push({ vt[st][i].b,vt[st][i].w });
		}
		while (!q.empty())
		{
			int b = q.top().b;
			int w = q.top().w;
			q.pop();
			if (vist[b] == 1)
				continue;
			if (kind[b] == 1)
				continue;
			else if (kind[b] == 2)
			{
				if (dis < w)
					dis = w;
				if (dis < res)
				{
					top = b;
					res = dis;
				}
				else if (dis == res)
				{
					if (b < top)
					{
						top = b;
						res = dis;
					}
				}
				break;
			}
			if (w > res)
				break;
			vist[b] = 1;
			if (dis < w)
				dis = w;
			for (int i = 0; i < vt[b].size(); i++)
			{
				if (vist[vt[b][i].b] == 0)
				{
					q.push({ vt[b][i].b,vt[b][i].w });
				}
			}
		}
		while (!q.empty())
			q.pop();
	}
	answer.push_back(top);
	answer.push_back(res);
	return answer;
}
int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);
	int n = 7;
	vector<vector<int>> paths = {{1, 2, 5}, {1, 4, 1}, {2, 3, 1}, {2, 6, 7}, {4, 5, 1}, {5, 6, 1}, {6, 7, 1}} ;
	vector<int> gates = {3,7};
	vector<int> summits = { 1,5 };
	solution(n, paths, gates, summits);
}

