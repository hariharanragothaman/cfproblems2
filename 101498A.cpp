/**
 * File              : 101498A.cpp
 * Author            : cppygod
 * Date              : 12.02.2022
 * Last Modified Date: 12.02.2022
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
#define stars cout << "***********************" << endl;

template<typename T>
void print(std::vector<T> const &v)
{
    for (auto i: v)
        cout << i << ' ';
    cout << endl;
}

bool sort_by_value(const pair<string, int> &a, const pair<string, int> &b)
{
    if(a.second == b.second)
    {
	    return (a.first < b.first);
    }
    else 
    {
	    return (a.second > b.second);
    }
}

void solve()
{
	int N; 
	cin >> N;
        string s;
	string f;
	unordered_map<string, int> H;	
	
	while(N--)
	{
		cin >> s >> f;
		H[f]++;
	}


        vector<pair<string, int>> vec;
        for(auto& elem: H)
        {
		vec.push_back(make_pair(elem.first, elem.second));
    	}
        sort(vec.begin(), vec.end(), sort_by_value);
        cout << vec[0].first << endl;
}

int32_t main()
{
    ENABLEFASTIO();
    int T;
    cin >> T;
    while(T--)
        solve();
}

