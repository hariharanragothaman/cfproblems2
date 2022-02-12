/**
 * File              : 1420A.cpp
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

	vector<int> arr(n, 0);
	vector<int> arr2(n, 0);
	set<int> s1;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
		arr2[i] = arr[i];
		s1.insert(arr[i]);
	}
	sort(arr.begin(), arr.end(), revsort);	
	
	//print(arr);
	//print(arr2);
	int counter = 0;
	for (int i = 0; i < n; i++)
	{
		if (arr[i] != arr2[i])
		{
			counter = 1;
			break;
		}
	}

	//cout << "The counter is:" << counter << endl;
	if (counter == 1 || s1.size() < n)
		cout << "YES" << endl;
	else
		cout << "NO" << endl;


}

int32_t main()
{
    ENABLEFASTIO();
    int T; 
    //T = 1;
    cin >> T;
    while(T--)
        solve();
}

