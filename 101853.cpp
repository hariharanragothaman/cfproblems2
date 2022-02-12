/**
 * File              : 101853.cpp
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
	int n, q;
	cin >> n >> q;
	vector<int> A(n, 0);
	unordered_map<int, int> H;
	for(int i=0; i<n; i++) 
	{
		cin >> A[i];
		H[A[i]]++;
	}

	int op, pos, value; 
	for(int i=0; i<q; i++)
	{
		cin >> op;
		if(op == 2)
		{
			H[0] += 1;
			cout << H.size() - 1 << endl;
		}

		else if(op == 1)
		{
			cin >> pos >> value;
			H[A[pos-1]] -= 1;
			if(H[A[pos-1]] == 0)
			{
				H.erase(A[pos-1]);
			}
			A[pos-1] = value;
			H[value] += 1;
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

