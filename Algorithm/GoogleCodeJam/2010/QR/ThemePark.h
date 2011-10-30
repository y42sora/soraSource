/*
 * ThemePark.h
 *
 *  Created on: 2011/04/07
 *      Author: y42sora
 */
#include <algorithm>
#include <fstream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

#define FOR(i,s,e) for (int i = int(s); i < int(e); i++)
#define FORIT(i,c) for (typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define ISEQ(c) (c).begin(), (c).end()

class Main {
public:
	int to_i (const string& str) {
	    int dec = 1;
	    int r_int = 0;

	    for (string::const_reverse_iterator it = str.rbegin(); it != str.rend(); it++) {
	        r_int += (static_cast<int>(*it) - '0') * dec;
	        dec *= 10;
	    }

	    return r_int;
	}

	bool deqEQ(deque<long long> a, deque<long long> b){
		deque<long long>::iterator nq = a.begin();
		deque<long long>::iterator sq = b.begin();
		while( nq != a.end() ){
			if(*sq != *nq) return false;
			sq++;
			nq++;
		}
		return true;
	}

	int check(vector< deque<long long> > start, deque<long long> now){
		FOR(i,0,start.size()){
			if(deqEQ(start[i],now)) return i;
		}
		return -1;
	}

	long long getS(vector<long long> ar, int z){
		long long sum = 0;
		FOR(i,z,ar.size())
			sum += ar[i];

		return sum;
	}

	void run(){
		ifstream ifs( "in.txt");
		string str;
		ifs >> str;

		int n = to_i(str);

		FOR(k,0,n){
			cout << "Case #" << k+1 << ": ";

			ifs >> str;
			int R = to_i(str);

			ifs >> str;
			int K = to_i(str);

			ifs >> str;
			int N = to_i(str);

			vector< deque<long long> > start;
			vector<long long> raid;

			deque<long long> now;

			FOR(i,0,N){
				ifs >> str;
				now.push_back(to_i(str));
			}
			start.push_back(now);

			int r = 0;
			for(int i=0; i<10000; i++){
				r++;
				int nin = 0;
				FOR(i,0,now.size()){
					if(K < nin + now.front() )
						break;
					nin += now.front();
					now.push_back(now.front());
					now.pop_front();
				}

				if(check(start,now) != -1){
					start.push_back(now);
					raid.push_back(nin);
					break;
				}
				start.push_back(now);
				raid.push_back(nin);
			}
			int z = check(start,now);
			long long loop = getS(raid,z);
			long long sum = 0;

			for(int i = 0; i <z && i < R; i++){
				sum += raid[i];
			}
			long long num = R - z;

			long long lnum = num / (raid.size()-z);
			sum += loop * lnum;

			int x = z;
			for(int i = 0; i < num % (raid.size()-z); i++){
				sum += raid[x++];
				if(x == raid.size())
					x = z+1;
			}

			cout << sum << endl;
		}
	}
};
