/**
 * File              : 291A.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 31.01.2022
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
	vector<int> A(n, 0);
	for(int i=0; i<n; i++)
	{
		cin >> A[i];
	}
	unordered_map<int, vector<int>> H;
        for(int i=0; i<n; i++)
	{
		H[A[i]].emplace_back(i);
	}	

	int cnt = 0;
	for(auto c: H)
	{
		if(c.first > 0 && c.second.size() > 2)
		{
			cout << "-1" << endl;
			return;
		}
		else if(c.first > 0 && c.second.size() == 2)
		{
		       cnt++;
		}	       
	}
	cout << cnt << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1; 
    //cin >> T;
    while(T--)
        solve();
}

