/*
 * AtCoder Regular Contest #006
 * D - アルファベット探し
 *
 *  Created on: 2012-07-21
 *      Author: y42sora
 *
 *  塊の個数を数えればいいらしい
 *  http://d.hatena.ne.jp/wotsushi/20120721/1342880968
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

int dir[8][2] = {
	{-1, -1},
	{-1,  0},
	{-1,  1},
	{ 0, -1},
	{ 0,  1},
	{ 1, -1},
	{ 1,  0},
	{ 1,  1}
};

bool is_inner(int x, int a, int b){
	if(a < x && x < b)
		return true;
	return false;
}

int dfs(int start_x, int start_y,int w, int h, VS &char_map)
{
	deque<PII> q;

	q.push_back(PII(start_x,start_y));

	int ans = 0;
	while(!q.empty()){

		PII p = q.front();
		q.pop_front();

		int x = p.first;
		int y = p.second;

		if (!is_inner(y, 0, h) || !is_inner(x, 0, w))
			continue;

		if(char_map[y][x] == '.')
			continue;

		char_map[y][x] = '.';
		ans++;
	
		REP(i,8)
			q.push_back(PII(x+dir[i][0], y+dir[i][1]));
	}

	return ans;
}

int main(void){
	int div[3] = {12,16,11};
	int ans[3] = {0,0,0};

	int h,w;
	cin >> h >> w;

	VS char_map;
	REP(i,h){
		string str;
		cin >> str;
		char_map.push_back(str);
	}

	

	REP(i,h){
		REP(j,w){
			if(char_map[i][j] == 'o'){
				int num = dfs(j,i,w,h,char_map);

				REP(k,3){
					int x=1;
					while(div[k] * x*x < num) x++;

					if(div[k] * x*x == num)
						ans[k]++;
				}
			}
		}
	}

	cout << ans[0] << " " << ans[1] << " " << ans[2] << endl;

	return 0;
}