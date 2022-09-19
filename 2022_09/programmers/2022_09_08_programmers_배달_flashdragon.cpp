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

int solution(int N, vector<vector<int> > road, int K) {
    int answer = 0;
    int dist[51];
    memset(dist, -1, sizeof(dist));
    vector<node>vt[51];
    priority_queue<node>pq;
    for (auto i : road)
    {
        int a = i[0];
        int b = i[1];
        int cost = i[2];
        vt[a].push_back({ b,cost });
        vt[b].push_back({ a,cost });
    }
    pq.push({ 1,0 });
    while (!pq.empty())
    {
        int a = pq.top().b;
        int cost = pq.top().cost;
        pq.pop();
        if (dist[a] != -1)
            continue;
        dist[a] = cost;
        cout << a << "\n";
        for (int i = 0; i < vt[a].size(); i++)
        {
            int b = vt[a][i].b;
            int ncost = vt[a][i].cost + cost;
            if (dist[b] == -1)
            {
                cout << "b:" << b << "\n";
                pq.push({ b,ncost });
            }
        }
    }
    for (int i = 1; i <= N; i++)
    {
        if (dist[i] != -1 && dist[i] <= K)
            answer++;
    }
    // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    return answer;
}
int main() {
    int n = 5;
    vector<vector<int>>road = { {1,2,1},{2,3,3},{5,2,2},{1,4,2},{5,3,1},{5,4,2} };
    int k = 3;
    cout << solution(n, road, k);
}