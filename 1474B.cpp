/**
 * File              : 1474B.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 23.01.2022
 * Last Modified By  : cppygod
 */

#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("inline")

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
vector<long long> sieve(int n) 
{
	int*arr = new int[n + 1](); 
	vector<long long> vect; 
	for (int i = 2; i <= n; i++)
		if (arr[i] == 0) 
		{
			vect.push_back(i); 
			for (int j = 2 * i; j <= n; j += i)
				arr[j] = 1;
		} 
	return vect;
}

long long  binary_searching(long long  a, vector<long long> &v1){
      int start = 0;
      int end = v1.size() - 1;
      long long  ans = 1e7;
      while(start <= end)
      {
            int mid = (start + end) / 2;
            if(v1[mid] >= a)
	    {
                  ans = min(ans, v1[mid]);
                  end = mid - 1;
            }
	    else
	    {
                  start = mid + 1;
            }
      }
      return ans;
}


void solve()
{
	vector<long long> primes = sieve(100000);
	long long d; 
	cin >> d;
	long long p1 = 1;
	long long  p2 = binary_searching(p1 + d, primes);
        long long  p3 = binary_searching(p2 + d, primes);
	cout << p1 * p2 * p3 << endl;

}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

