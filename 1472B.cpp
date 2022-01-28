/**
 * File              : 1472B.cpp
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
	vector<int> A(n, 0);
	long long sum = 0;
	unordered_map<int, int> H; 
	for(int i=0; i<n; i++)
	{
		cin >> A[i];
		sum += A[i];
		H[A[i]] += 1;
	}

	if( sum & 1 )
	{
		cout << "NO" << endl;
		return;
	}
	else 
	{
		/* Possible Case Scenarios
		 * 2 2 2 1 1 1
		 * 2 2 2 1 1
		 * 2 1 1 1 1
		 */

		if(H[1] == 0 && H[2] % 2 != 0)
		{
			cout << "NO" << endl;
		}
		else if(H[2] == 0 && H[1] % 2 != 0)
		{
			cout << "NO" << endl;
		}
		else if(H[2] > 0 && H[2] % 2 != 0 && H[1] > 0 && H[1] % 2 != 0 )
		{
			cout << "NO" << endl;
		}
		else 
		{
			cout << "YES" << endl;
		}

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

