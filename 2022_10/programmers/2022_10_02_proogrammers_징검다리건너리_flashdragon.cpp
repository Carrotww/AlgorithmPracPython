#include <string>
#include <vector>

using namespace std;
bool go(vector<int> stones, int k, int m)
{
	int cnt = 1;
	for (int i : stones)
	{
		if (i >= m)
		{
			cnt = 1;
		}
		else
		{
			cnt++;
			if (cnt > k)
				return false;
		}
	}
	return true;
}
int solution(vector<int> stones, int k) {
	int answer = 0;
	int low = 0;
	int high = 0;
	for (int i : stones)
	{
		if (i > high)
			high = i;
	}
	high++;
	while (low < high)
	{
		int mid = (low + high) / 2;
		if (go(stones, k, mid))
		{
			low = mid + 1;
		}
		else
		{
			high = mid;
		}
	}
	answer = high - 1;
	return answer;
}