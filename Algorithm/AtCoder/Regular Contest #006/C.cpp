/*
 * AtCoder Regular Contest #006
 * C - Ï‚İd‚Ë
 *
 *  Created on: 2012-07-21
 *      Author: y42sora
 *
 *  æÃ—~–@‚Å
 *  ’u‚¯‚éê‡‚ÍÅ‚à¬‚³‚¢‚à‚Ì‚Ìã‚É‰œ‚Ì‚ªÅ¬
 *  Å‰‚Ì}‚Íã©
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

bool put(VI &boxes, int in){
	REP(i,boxes.size()){
		if(in <= boxes[i]){
			boxes[i] = in;
			return true;
		}
	}
	return false;
}

int main(void){
	int n;
	cin >> n;

	VI boxes;
	REP(i,n){
		int in;
		cin >> in;
		if(!put(boxes, in))
			boxes.push_back(in);

		SORT(boxes);
	}

	cout << boxes.size() << endl;

	return 0;
}