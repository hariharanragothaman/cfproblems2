/**
 * File              : most_frequent_substring.cpp
 * Author            : cppygod
 * Date              : 23.01.2022
 * Last Modified Date: 24.01.2022
 * Last Modified By  : cppygod
 */


#include "bits/stdc++.h"
using namespace std;
#define ENABLEFASTIO() ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL)

#define ONLINE_JUDGE   /* IF not ONLINE_JUDGE Comment this line*/

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

#define mod 1000000007

int computeRollingHash(string s,int l,int r)
{
	s=s.substr(l,r-l+1);
	long long  n=s.size();

	int p=31;
	int p_power=1;
	long long hashValue=0;

	for(long long i=0;i<n;i++)
	{
	    long long adder= ( (s[i]-'a'+1) * p_power)%mod;
	    hashValue= (hashValue + adder)%mod;

	    p_power=(p_power * p)%mod;
	}
	return hashValue;
}

long long countUniqueChars(int i, int j, int freq[][26])
{
	long long count = 0;
	for(int k=0; k<26; k++)
	{
		long long charCount = freq[j][k] - ((i==0)?0:freq[i-1][k]);
		if(charCount)
			count++;
	}
	return count;
}

void solve()
{
	string s;
	cin >> s;
	int minl, maxl, maxu;
	cin >> minl >> maxl  >> maxu;
	long long n = s.size();

	int freq[n][26];
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<26;j++)
		{
			freq[i][j] = 0;
		}
	}

	for(int i=0; i<n; i++)
	{
		freq[i][s[i]-'a']++;
	}

	int k = minl;
	map<long long, long long> umap;
	long long  maxCount=0;


	for(int i=0;i<=n-k;i++)
	{
	    int j=i+k-1;

	    int countChar= countUniqueChars(i,j,freq);

	    if(countChar > maxu )
		    continue;

	    long long ans=computeRollingHash(s,i,j);

	    if(umap.find(ans)==umap.end())
	    {
		umap[ans]=1;
	    }
	    else
	    {
		umap[ans]++;
		maxCount=max(maxCount,umap[ans]);
	    }
	}

	for(auto c: umap)
	{
		cout << c.first << " " << c.second << endl;
	}
	cout<<maxCount+1<<"\n";

	}

int32_t main()
{
    ENABLEFASTIO();
    int T = 1;
    while(T--)
        solve();
}

