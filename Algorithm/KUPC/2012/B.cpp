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
	string st;
	cin >> st;

	if(st[0] == 'o' && st[st.length()-1] == 'x')
		cout << 'o' << endl;
	if(st[0] == 'x' && st[st.length()-1] == 'o')
		cout << 'o' << endl;
	if(st[0] == 'o' && st[st.length()-1] == 'o')
		cout << 'o' << endl;
	if(st[0] == 'x' && st[st.length()-1] == 'x')
		cout << 'x' << endl;
	return 0;
}