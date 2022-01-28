/*
* @Author: Hariharan Ragothaman
* @Date:   2022-01-11 10:02:46
* @Last Modified by:   Hariharan Ragothaman
* @Last Modified time: 2022-01-12 07:36:10
*/

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

// #define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

#ifndef ONLINE_JUDGE
ifstream  i_data("../io/data.in");
ofstream  o_data("../io/data.out");
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
	int n, k;
	cin >> n >> k;
	vector<int> arr(n, 0);
	for(int i=0; i<n; i++)
		cin >> arr[i];

	int itr = *max_element(arr.begin(), arr.end());
    int p = log2(itr) + 1;
 
    int X = 0;
    for (int i = 0; i < p; i++) 
    {
        int count = 0;
        for (int j = 0; j < n; j++) 
        {
            if (arr[j] & (1 << i)) 
                count++;
        }
        if (count > (n / 2)) 
        {
            X += 1 << i;
        }
    }
 
    int sum = 0;
    for (int i = 0; i < n; i++)
        sum += (X ^ arr[i]);
 
    cout << X << endl;

}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

