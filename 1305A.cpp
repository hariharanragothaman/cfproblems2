/**
 * File              : 1305A.cpp
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


	vector<int> A (n, 0), B(n, 0);
	for(int i=0; i<n; i++) cin >> A[i];
	for(int i=0; i<n; i++) cin >> B[i];

	sort(A.begin(), A.end());
	sort(B.begin(), B.end());
	print(A);
	print(B);


}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    cin >> T;
    while(T--)
        solve();
}

