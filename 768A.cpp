/**
 * File              : 768A.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 04.02.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
#include <numeric> 
using namespace std;

// #define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("data.in");
ofstream  o_data("data.out");
#define cin  i_data
#define cout o_data
#else
#endif


#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)
#define int long long
#define stars cout << "********************************" << endl;
#define debug(a)  cout << a << endl;
#define MOD 1000000007

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}


bool comparator(pair<int, int> A, pair<int, int> B)
{
	return (A.first < B.first);
}

// Putting all the odd numbers first
bool cmp(int a , int b)
{
	return a % 2 < b % 2;
}

bool revsort(int a, int b) 
{
	return a > b;
}

void solve()
{
	int n;
        cin >> n;	
	vector<int> A(n, 0);
	for(int i=0; i<n; i++)
		cin >> A[i];

	int minn = *min_element(A.begin(), A.end());
	int maxx = *max_element(A.begin(), A.end());


	unordered_map<int, int> H; 
	int cnt = 0;
	for(auto c: A)
	{
		H[c]++;
	}

	for(auto c: H)
	{
		if(c.first != minn && c.first != maxx)
		{
			cnt += c.second; 
		}
	}

	cout << cnt << endl;

}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    T = 1;
    //cin >> T;
    while(T--)
        solve();
}

