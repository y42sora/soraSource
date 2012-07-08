/*
 * KUPC
 * D - å†óÕ
 *
 *  Created on: 2012-07-01
 *      Author: y42sora
 *
 * Ê√ó~ñ@Ç≈ç∂Ç©ÇÁéÊÇ¡ÇƒÇ¢Ç≠
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


int main(void){
	int n,m;
	cin >> n >> m;

	vector<PII> doctor;
	REP(i,m){
		int a,b;
		cin >> a >> b;
		doctor.push_back(PII(b,a));
	}

	sort(doctor.begin(),doctor.end(),greater<PII >());

	int now = 1;
	int result = 0;
	while(true){
		int pos = now;
		REP(i,doctor.size()){
			int b = doctor[i].first;
			int a = doctor[i].second;

			if( a <= pos && pos <= b){
				pos = b+1;
				break;
			}
		}
		if(pos == now){
			cout << "Impossible" << endl;
			return 0;
		}

		result++;
		now = pos;

		if(n < now)
			break;
	}

	cout << result << endl;
	return 0;
}