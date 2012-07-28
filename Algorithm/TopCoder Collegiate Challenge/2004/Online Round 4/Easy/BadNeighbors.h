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

class BadNeighbors {

	public: int maxDonations(vector<int> donations) {

		int big = 0;

		int **memo = new int*[2];
		memo[0] = new int[donations.size()];
		memo[1] = new int[donations.size()];

		FOR(i,0,donations.size()) {
			memo[0][i] = 0;
			memo[1][i] = 0;
		}

		memo[0][0] = donations[0];
		memo[1][0] = 0;

		FOR(i,1,donations.size()-1){
			memo[0][i] = memo[1][i-1] + donations[i];
			memo[1][i] = max(memo[1][i-1], memo[0][i-1]);

			big = max(big,max(memo[0][i],memo[1][i]));
		}

		memo[0][0] = 0;
		memo[1][0] = 0;

		FOR(i,1,donations.size()){
			memo[0][i] = memo[1][i-1] + donations[i];
			memo[1][i] = max(memo[1][i-1], memo[0][i-1]);

			big = max(big,max(memo[0][i],memo[1][i]));
		}


		return int(big);
	}

};
