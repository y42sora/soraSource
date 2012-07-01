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
typedef long long LL;
const double EPS = 1e-10;
#define SORT(c) sort((c).begin(),(c).end())

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;


int main(void){
	int n,k,r;
	cin >> n >> k;

	VVI boat;
	REP(i,k){
		VI line;
		int m;
		cin >> m;
		REP(i,m){
			int b;
			cin >> b;
			line.push_back(b);
		}
		boat.push_back(line);
	}

	VVB bad;
	REP(i,n+1){
		VB bad_line;
		REP(j,n+1)
			bad_line.push_back(false);
		bad.push_back(bad_line);
	}

	cin >> r;
	REP(i,r){
		int p,q;
		cin >> p >> q;

		bad[p][q] = true;
		bad[q][p] = true;
	}

	VB usa;
	REP(i,n+1)
		usa.push_back(false);

	REP(i,boat.size())
		REP(j,boat[i].size())
			REP(k,boat[i].size())
				if(bad[boat[i][j]][boat[i][k]])
					usa[boat[i][j]] = true;

	int res = 0;
	REP(i,n+1)
		if(usa[i])
			res++;

	cout << res << endl;

	return 0;
}