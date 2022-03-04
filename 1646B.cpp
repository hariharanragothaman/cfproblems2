/**
 * File              : B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 04.03.2022
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

	sort(A.begin(),A.end());

	int i = 1; 
	int j = n -1; 
	int lsum = A[0];
	int rsum = 0;

	while(i<j)
	{
		lsum += A[i];
		rsum += A[j];

		if (lsum < rsum)
		{
			cout << "YES" << endl;
			return;
		}

		i++;
		j--;
	}

	cout << "NO" << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

