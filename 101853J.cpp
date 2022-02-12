/**
 * File              : 101853J.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 11.02.2022
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
	vector<int> A(n, 0);
	unordered_map<int, int> H;
	for(int i=0; i<n; i++) 
	{
		cin >> A[i];
		H[A[i]]++;
	}
	int cnt = 0; 
	int mx = 0;
	for(int i=2; i<=10000; i++)
	{
		cnt = H[i] + H[i-1];
		mx = max(mx, cnt);
	}
	cout << mx << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

