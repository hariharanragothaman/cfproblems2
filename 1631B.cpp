/**
 * File              : 1631B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 27.01.2022
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
	for(int i=0; i<n; i++) 
		cin >> A[i];
	
	int i = n-1;
	int candidate = A[i];
	i--;
	
	int s = 1;
	int output = 0;
	
	while(i > -1)
	{
		bool same = true;
		while(i>-1 && A[i] == candidate)
		{
		    i--;
		    s++;
		}

		for(int j=i; j>i-s && j>-1; j--)
		{
		    if(A[j] != candidate)
		    {
			same = false;
		    }
		}

		if(!same)
		    output++;

		i = i-s;
		s = s*2;
	}
	cout << output << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

