/*
 * AtCoder Regular Contest #006
 * B - ‚ ‚Ý‚¾‚­‚¶
 *
 *  Created on: 2012-07-21
 *      Author: y42sora
 *
 * ‰º‚©‚ç’H‚Á‚Ä‚¢‚­‚¾‚¯
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
	int n,l;
	cin >> n >> l;

	VS maze;
	string buf;
	getline(cin, buf);
	REP(i,l){
		getline(cin, buf);
		maze.push_back(buf);
	}

	string goal;
	getline(cin, goal);

	int x,y;

	x = goal.find_first_of('o');
	y = l-1;

	while(0 <= y){
		// left
		if(x != 0){
			if(maze[y][x-1] == '-'){
				x -= 2;
				y -= 1;
				continue;
			}
		}

		// right
		if(x != maze[y].size()-1){
			if(maze[y][x+1] == '-'){
				x += 2;
				y -= 1;
				continue;
			}
		}

		y -= 1;
	}

	cout << (x/2)+1 << endl;

	return 0;
}