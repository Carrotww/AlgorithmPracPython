#include <string>
#include <vector>
#include <iostream>

using namespace std;
long long fun(vector<int> times, long long t)
{
	long long res = 0;
	for (int i : times)
	{
		res = res + t / i;
	}
	return res;
}

long long solution(int n, vector<int> times) {
	long long answer = 0;

	long long low = 1;
	long long high = 1;
	for (int i : times)
	{
		if (high < n * i)
			high = n * i;
	}
	while (low < high)
	{
		long long mid = (low + high) / 2;
		if (n > fun(times, mid))
		{
			low = mid + 1;
		}
		else
			high = mid;
	}
	answer = high;
	return answer;
}