/**
 * File              : C.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 04.03.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
using ll = long long;
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

ll factorial(ll n)
{
    if (n == 0)
        return 1;
    return n * factorial(n - 1);
}

ll dp [100];
const int MOD = (int) 1e9 + 7;

void solve()
{
	int value; 
	cin >> value; 
	set<ll> s;
	for(int i=1;i<45;i++)
	{
		s.insert(1LL<<i);
	}
	for(int i=1;i<18;i++)
	{
		s.insert(factorial(i));
	}

	vector<ll> coins;
	for(auto c: s)
	{
		coins.push_back(c);
	}
	print(coins);

	dp[0] = 1;
	for (int i = 1; i <= coins.size(); i++) 
	{
		for (int weight = 0; weight <= value; weight++) 
		{
			if(weight - coins[i - 1] >= 0) 
			{  	// prevent out of bounds cases
				dp[weight] += dp[weight - coins[i - 1]];
				dp[weight] %= MOD;
			}
		}
	}
	
	for(auto c: dp)
	{
		cout << c << " ";
	}
	cout << endl;
	cout << dp[value] << '\n';
	stars
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

