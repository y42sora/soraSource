/*
 * Facebook Hacker Cup 2012 Round 1
 * Checkpoint
 *
 *  Created on: 2012/01/29
 *      Author: y42sora
 *
 * 前半でできる限り近づいて，後半でぴったりに調整
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <fstream>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef pair<double, double> PDD;
typedef long long LL;
const double EPS = 1e-10;
#define SORT(c) sort((c).begin(),(c).end())

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;

// comb
LL comb(int n, int r){
	if(r==0 || r==n)
		return (1);
	else if(r==1)
		return (n);
	return (comb(n-1, r-1) + comb(n-1, r));
}

int main(void){
	ifstream cin("in.txt");
	FILE *fp = fopen("output.txt", "w");

	int n;
	cin >> n;

	REP(i,n){
		LL s;
		cin >> s;

		// 割り切れて最大の物を探す，割り切れなかったら0,1へ移動したことにする
		int a = 1;
		int x = 1;
		int y = 0;
		while(true){
			LL size = comb(a+a,a);
			if(s <= size) break;

			if(s % size == 0){
				x = a;
				y = a;
			}
			a++;
		}

		int t = x+y;
		s = s / comb(x+y,y);

		a=1;
		x=1;
		y=0;
		while(true){
			LL size = comb(a+a,a);
			if(s < size) break;
			x = a;
			y = a;
			a++;	
		}

		while(true){
			LL size = comb(x+y,y);
			if(size == s) break;

			LL next = comb(x+1+y,y);
			if(s < next){
				y--;
				continue;
			}
			x++;
		}

		t += x+y;

		fprintf( fp, "Case #%d: %d\n", i+1, t);

	}

	fclose(fp);

	return 0;
}
