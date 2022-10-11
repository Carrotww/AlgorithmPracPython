#include <string>
#include <vector>
#include <queue>
using namespace std;
queue<pair<int, int>>q;
int solution(int bridge_length, int weight, vector<int> truck_weights) {
	int answer = 0;
	int w = 0;
	int time = 0;
	int id = 0;
	while (1)
	{
		time++;
		if (q.front().second + bridge_length == time)
		{
			w -= q.front().first;
			q.pop();
		}
		if (w + truck_weights[id] <= weight)
		{
			q.push({ truck_weights[id],time });
			w += truck_weights[id];
			id++;
		}
		if (id == truck_weights.size())
		{
			time += bridge_length;
			break;
		}
	}
	answer = time;
	return answer;
}