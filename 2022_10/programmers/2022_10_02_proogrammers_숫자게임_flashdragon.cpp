#include <string>
#include <vector>
#include <algorithm>

using namespace std;
bool cmp(int a, int b)
{
	return a > b;
}
int solution(vector<int> A, vector<int> B) {
	int answer = -1;
	int n = A.size();
	sort(A.begin(), A.end(), cmp);
	sort(B.begin(), B.end(), cmp);
	int a = 0;
	int b = 0;
	answer = 0;
	while (a < n && b < n)
	{
		if (A[a] < B[b])
		{
			answer++;
			a++;
			b++;
		}
		else
		{
			a++;
		}
	}
	return answer;
}