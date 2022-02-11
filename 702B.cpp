/**
 * File              : 702B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 10.02.2022
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

void solve()
{
	int n; 
	cin >> n;
	vector<int> A (n, 0);
	for(int i=0; i<n; i++) 
		cin >> A[i];
	
	vector<int> P; 
	for(int i=1; i<=30; i++)
		P.push_back((1 << i));

	unordered_map<int, vector<int>> H; 
	for(int i=0; i<n; i++)
		H[A[i]].emplace_back(i);

	int cnt = 0;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<=P.size(); j++)
		{
			int diff = P[j] - A[i];
			if(H.count(diff) > 0)
			{
				vector<int> pos = H[diff];
				for(auto idx: pos)
				{
					if( idx > i )
					{
						cnt++;
					}
				}
			}
		}
	}
	cout << cnt << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1; 
    while(T--)
        solve();
}

