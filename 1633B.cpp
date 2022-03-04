/**
 * File              : 1633B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 31.01.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
#include <unordered_map>
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


void solve()
{
	string s;
	cin >> s;
	unordered_map<char, int> H;
	for(auto c: s)
	{
		H[c]++;
	}

	if(H['0'] > H['1'])
	{
		cout << H['1'] << endl;
	}
	else if(H['0'] < H['1'])
	{
		cout << H['0'] << endl;
	}
	else if(H['0'] == H['1'])
	{
		// Choose a subsegment greedily where one of them is greater and then 
		// and cover how much ever 1's until it doesn't exceed

		int n = s.size();
		int opp_cnt = 0;

		int i = 0;
		while( i < n )
		{
			if(s[i] != s[0] and opp_cnt < H[s[i]] - 1)
			{
				opp_cnt++;
				i++;
			}
			else if(s[i] == s[0])
			{
				i++;
			}
			else 
			{
				break;
			}

		}
		int ans = 0;
		for(int j = 0; j < i; j++)
		{
			if(s[j] != s[0])
			{
				ans++;
			}		
		}
		cout << ans << endl;
	}
}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    cin >> T;
    while(T--)
        solve();
}

