/**
 * File              : A.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 23.01.2022
 * Last Modified By  : cppygod
 */

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

#include <iostream>
#include <fstream>
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <chrono>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

// For Hash
#include <functional>

// For all useful constants
#include <climits>

// Data-Structures and related stuff.
#include <map>
#include <set>
#include <stack>
#include <random>
#include <deque>
#include <queue>   // Includes Priority Queue
#include <vector>
#include <unordered_map>
#include <unordered_set>

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
	int n, x;
	cin >> n >> x;
	vector<int> A(n, 0);
	for(int i=0; i<n; i++)
	{
		cin >> A[i];
	}
	int k;
	cin >> k; 
	vector<int> B(k, 0);
	int interest = 0;
	for(int i=0; i<k; i++)
	{
		int a; 
		cin >> a;
		a = a - 1; 
		interest += A[a];
	}

	cout << x - interest + 1 << endl;


}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

