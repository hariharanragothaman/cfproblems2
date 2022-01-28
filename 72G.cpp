/**
 * File              : 72G.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 24.01.2022
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
#else
#endif


#define int long long

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

void solve()
{
	int n; 
	cin >> n; 
	vector<int> A(n+1, 0);
	A[0] = 1;
	A[1] = 1;

	for(int i=2; i<=n; i++)
	{
		A[i] = A[i-1] + A[i-2];
	}
	cout << A[n] << endl;;
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

