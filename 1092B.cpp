/**
 * File              : 1092B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 26.01.2022
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
	/*
	 *
	 * 6 students - 3 teams of each - So we pair of students.
	 * 2 students can form a team, only if their skill are equal
	 */

	sort(A.begin(), A.end());
	int diff = 0;
	for(int i=1; i<n; i+=2)
	{
		diff += A[i] - A[i-1];
	}
	cout << diff << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

