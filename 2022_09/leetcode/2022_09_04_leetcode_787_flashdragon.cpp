
struct go {
	int b, cost = -1;
	int time = -1;
	bool operator<(const go& temp)const {
		return cost > temp.cost;
	}
};
vector<go>vt[101];
int check[101] = { 0 };
int vist[101][101];
priority_queue<go>q;
class Solution {
public:

	int findCheapestPrice(int n, vector<vector<int>>& flights, int src, int dst, int k) {
		while (!q.empty())
			q.pop();
		memset(vist, -1, sizeof(vist));
		memset(check, 0, sizeof(check));
		for (int i = 0; i < n; i++)
		{
			vt[i].clear();
		}
		for (auto t : flights)
		{
			vt[t[0]].push_back({ t[1],t[2] });
		}
		q.push({ src,0,0 });
		while (!q.empty())
		{
			int st = q.top().b;
			int cost = q.top().cost;
			int time = q.top().time;
			q.pop();
			if (time > k + 1)
				continue;
			if (st == dst)
			{
				return cost;
			}
			for (int i = 0; i < vt[st].size(); i++)
			{
				int d = vt[st][i].b;
				int ncost = vt[st][i].cost + cost;
				int ntime = time + 1;
				if (vist[d][ntime] == -1 || vist[d][ntime] > ncost)
				{
					vist[d][ntime] = ncost;
					q.push({ d,ncost,ntime });
				}
			}
		}
		int res = -1;
		for (int i = 1; i <= k + 1; i++)
		{
			if (vist[dst][i] != -1 && (res == -1 || vist[dst][i] < res))
				res = vist[dst][i];
		}
		return res;
	}
};