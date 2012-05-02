/*
 * GCJ
 *
 *  Created on: 2012/04/14
 *      Author: y42sora
 * 
 * 入れ替えて範囲内かを繰り返す
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

int main(void){
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	int n;
	cin >> n;

	REP(i,n){
		LL a,b,count;
		cin >> a;
		cin >> b;
		count=0;

		LL x = 1;
		for(LL y = a; y != 0; x*=10)
			y /= 10;
		x /= 10;

		FOR(j,a,b){
			LL z=j/10 + x*(j%10);
			while(z!=j){
				if(a <= z && z <= b && j<z){
					count++;
				}
				z = z/10 + x*(z%10);
			}
		}

		cout << "Case #" << (i+1) << ": " << count << endl;
	}
	return 0;
}