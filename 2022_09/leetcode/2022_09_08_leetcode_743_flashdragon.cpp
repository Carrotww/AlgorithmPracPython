#include <iostream>
#include <vector>
#include <cstring>
#include <queue>
using namespace std;
struct node {
    int b, cost;
    bool operator<(const node& temp)const {
        return cost > temp.cost;
    }
};
int dist[101];
vector<node>vt[101];
priority_queue<node>pq;
class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        int answer = -1;
        memset(dist, -1, sizeof(dist));
        while (!pq.empty())
            pq.pop();
        for (int i = 1; i <= n; i++)
            vt[i].clear();
        for (auto i : times)
        {
            int a = i[0];
            int b = i[1];
            int cost = i[2];
            vt[a].push_back({ b,cost });
        }
        pq.push({ k,0 });
        while (!pq.empty())
        {
            int a = pq.top().b;
            int cost = pq.top().cost;
            pq.pop();
            if (dist[a] != -1)
                continue;
            dist[a] = cost;
            for (int i = 0; i < vt[a].size(); i++)
            {
                int b = vt[a][i].b;
                int ncost = vt[a][i].cost + cost;
                if (dist[b] == -1)
                {
                    pq.push({ b,ncost });
                }
            }
        }
        for (int i = 1; i <= n; i++)
        {
            if (dist[i] == -1)
            {
                answer = -1;
                break;
            }
            else
            {
                if (answer == -1 || answer < dist[i])
                    answer = dist[i];
            }
        }

        return answer;
    }
};