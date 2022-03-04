/**
 * File              : 1594B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 29.01.2022
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
#define stars cout << "********************************" << endl;

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

#define MOD 1000000007

void solve()
{
	int n, k;
	cin >> n >> k;
	int p = 1;
	int ans = 0;

	for(int i=0; i<31; i++)
	{
		// Checking if that bit has been set for k
		if( k & (1 << i) )
		{
			ans = (ans + p) % MOD;
		}

		p = p * n;
		p = p % MOD;
	}

	cout << ans << endl;
	//stars
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

