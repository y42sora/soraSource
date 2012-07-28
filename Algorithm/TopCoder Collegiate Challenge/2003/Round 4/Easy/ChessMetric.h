#include <algorithm>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i != int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

class ChessMetric {



	long long getNum(long long***dp, int i,int j,int k,int size){
		int xm[] = {-1, 1,-2,-1, 0, 1, 2,-1,1,-2,-1,0,1,2,-1,1};
		int ym[] = {-2,-2,-1,-1,-1,-1,-1, 0,0, 1, 1,1,1,1, 2,2};

		long long num = 0;

		FOR(a,0,16){
			int x = i + xm[a];
			int y = j + ym[a];
			if(x < 0) continue;
			if(size <= x)continue;
			if(y < 0)continue;
			if(size <= y)continue;

			num += dp[x][y][k-1];
		}
		return num;
	}

	public: long long howMany(int size, vector<int> start, vector<int> end, int numMoves) {
		long long ***dp = new long long**[size];
		FOR(i,0,size){
			dp[i] = new long long*[size];
			FOR(j,0,size){
				dp[i][j] = new long long[numMoves+1];
				FOR(k,0,numMoves+1){
					dp[i][j][k] = 0;
				}
			}
		}

		dp[start[0]][start[1]][0] = 1;

		FOR(k,1,numMoves+1)
			FOR(i,0,size)
					FOR(j,0,size)
						dp[i][j][k] = getNum(dp,i,j,k,size);


		return dp[end[0]][end[1]][numMoves];
	}

};
