/**
 * File              : 149A.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 03.02.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

// #define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
50
2 2 3 4 5 4 4 5 7 3 2 7#else
#endif


#define int long long
#define stars cout << "********************************" << endl;

#define debug(a)  cout << a << endl;

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}


bool comparator(pair<int, int> A, pair<int, int> B)
{
	return (A.first < B.first);
}

void solve()
{
	int k;
	cin >> k;
	vector<int> A(12, 0); 
	for(int i=0; i < A.size(); i++)
	{
		cin >> A[i];
	}
	sort(A.begin(), A.end());
	reverse(A.begin(), A.end());
	int sum = 0;
	int cnt = 0;
	for(int i=0; i < A.size() && sum < k ; i++)
	{
			sum += A[i];
			cnt++;
	}
	if(sum >= k)
	{
		debug(cnt);
	}
	else
	{	
		debug(-1);
		
	}
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

