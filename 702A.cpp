/**
 * File              : 702A.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 09.02.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
#include <numeric> 
using namespace std;

//#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
#else
#endif


#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int long long
#define stars cout << "********************************" << endl;
#define debug(a)  cout << a << endl;
#define MOD 1000000007
#define all(x) x.begin(), x.end()


void solve()
{
	int n; 
	cin >> n; 
	vector<int> A(n+1, 0);
	for(int i=0; i<n; i++)
	{
		cin >> A[i];
	}
	int cnt = 0;
	int mx = 0;

	for(int i=0; i<n; i++)
	{
		if(i==0 || A[i] > A[i-1])
		{
			cnt += 1;
		}
		else 
		{
			cnt = 1;
		}
		mx = max(mx, cnt); 
	}
	debug(mx);

}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    T = 1;
    while(T--)
        solve();
}
