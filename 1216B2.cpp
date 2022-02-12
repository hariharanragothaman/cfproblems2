/**
 * File              : 1216B2.cpp
 * Author            : cppygod
 * Date              : 04.02.2022
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
	std::vector<int> A(n, 0);
	for(int i=0; i<n; i++) cin >> A[i];

	std::vector<int> B(n, 0);
	for(int i=0; i<n; i++)
	{
		B[i] = A[i];
	}
	sort(all(A), revsort);

	int ans = 0;
	for(int i=0; i<n; i++)
	{
		int val = A[i] * (i) + 1;
		ans += val;
	}

	debug(ans);

	unordered_map<int, vector<int>> H;
	for(int i=0; i<n; i++)
	{
		H[B[i]].push_back(i);
	}
	/*
	cout << "Printing the Hashmap" << endl;
	for(auto c: H)
	{
		cout << c.first << " : ";
		for(auto k: c.second)
			cout << k << " ";
		cout << endl;
	}
	*/

	vector<int> result;
	for(auto val: A)
	{
		//cout << "The val now is: " << val << endl;
		for(auto c : H[val])
		{
			if(find(all(result), c) == result.end())
			{
				//cout << "The value of c is:" << c << endl;
				result.push_back(c);
				break;
			}
		}
	}

	for(auto c: result)
	{
		cout << c+1 <<  " ";
	}
	cout << endl;
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
