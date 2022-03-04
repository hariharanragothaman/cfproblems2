/**
 * File              : 1633A.cpp
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
	int n; 
	cin >> n;
	vector<int> ff;
	
	for(int i=2; i<1001; i++) ff.push_back(i*7);
	
	if(count(ff.begin(), ff.end(), n) > 0)
	{
		cout << n << endl;
	}
	else 
	{
		int idx = lower_bound(ff.begin(), ff.end(), n) - ff.begin();
		if(idx == 0)
		{
			cout << ff[idx] << endl;
		}
		else	
		{
			string cd1 = to_string(ff[idx-1]);
			string cd2 = to_string(ff[idx]);
			string nn = to_string(n);
		
			int cnt1 = 0;
			int cnt2 = 0;

			for(int i=0; i<nn.size(); i++)
			{
				if(nn[i] != cd1[i])
				{
					cnt1++;
				}
			}

			for(int i=0; i<nn.size(); i++)
			{
				if(nn[i] != cd2[i])
				{
					cnt2++;
				}
			}

			
			if(cnt1 <= cnt2)
			{
				cout << cd1 << endl;
			}
			else 
			{
				cout << cd2 << endl;
			}
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

