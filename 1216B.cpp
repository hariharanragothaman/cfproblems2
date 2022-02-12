/**
 * File              : 1216B.cpp
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
#define all(x) x.begin(), x.end()

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

int compute(int a, int b, int c)
{
	return abs(a-b) + abs(a-c) + abs(b-c);
}

void solve()
{
    int n;
    cin >> n;
    vector<pair<int, int>> a(n);
    for (int i = 0; i < n; ++i) 
    {
        cin >> a[i].first;
        a[i].second = i;
    }
    sort(a.begin(), a.end(), greater<pair<int, int>>());
    int ans = 0;
    for (int i = 0; i < n; ++i) 
    {
        ans += i * a[i].first + 1;
    }
    cout << ans << '\n';
    for (int i = 0; i < n; ++i) 
    {
        cout << a[i].second + 1;
        if (i < n - 1)
            cout << ' ' ;
    }
    cout << '\n';
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
