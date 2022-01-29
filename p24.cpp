/**
 * File              : p24.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 28.01.2022
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

	// The key property in bubble sort is - last i elements are already in-place
	for(int i=1; i<n; i++)
	{
	    for(int j=1; j<n; j++)
	    {
		if( A[j] < A[j-1])
		{
			swap(A[j], A[j-1]);
		}
	    }	
	   print(A);
	}
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

