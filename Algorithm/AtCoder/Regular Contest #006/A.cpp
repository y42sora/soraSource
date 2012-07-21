/*
 * AtCoder Regular Contest #006
 * A - 宝くじ
 *
 *  Created on: 2012-07-21
 *      Author: y42sora
 *
 * 合ってる個数を数えてボーナス数字が合ってるかどうかを調べて別判断
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
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<double> VD;
typedef long long LL;
const double EPS = 1e-10;
#define SORT(c) sort((c).begin(),(c).end())

int check(VI entry, VI lot){
	int count = 0;
	REP(i,entry.size())
		REP(j,lot.size())
			if(entry[i] == lot[j])
				count++;
	return count;
}

int main(void){
	VI entry;
	VI bornus;
	VI lot;

	REP(i,6){
		int in;
		cin >> in;
		entry.push_back(in);;
	}

	int b;
	cin >> b;
	bornus.push_back(b);
	
	REP(i,6){
		int in;
		cin >> in;
		lot.push_back(in);
	}

	int num = check(entry, lot);

	int ans = 0;
	switch(num){
	case 6:
		ans = 1;
		break;
	case 5:
		if(check(lot, bornus) == 1)
			ans = 2;
		else
			ans = 3;
		break;
	case 4:
		ans = 4;
		break;
	case 3:
		ans = 5;
		break;
	}

	cout << ans << endl;

	return 0;
}