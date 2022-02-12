/**
 * File              : 101498B.cpp
 * Author            : cppygod
 * Date              : 12.02.2022
 * Last Modified Date: 12.02.2022
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
#define stars cout << "***********************" << endl;

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

void solve()
{
	string s, t;
	cin >> s >> t;
	unordered_map<char, int> T;
	for(auto c: t) T[c]++;
	int cnt = 0;
	// Check if you can form a from b 
	for(auto c: s)
	{
		if( T[c] > 0 )
		{
			cnt += 1;
			T[c] -= 1;
		}
		else 
		{
			break;
		}
	}
	cout << cnt << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

