#include <algorithm>
#include <iostream>
#include <fstream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
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
	void run(){
		ifstream ifs( "in.txt");
		string str;
		ifs >> str;

		int n = to_i(str);

		FOR(i,0,n){
			cout << "Case #" << i+1 << ": ";
			ifs >> str;

			int x = to_i(str);
			vector<int> b;
			vector<int> r;

			FOR(j,0,x){
				ifs >> str;
				int num = to_i(str.substr(0,str.size()-1));

				if(str[str.size()-1] == 'B')
					b.push_back(num);
				else
					r.push_back(num);
			}


			int small = min(b.size(),r.size());

			if(small == 0){
				cout << 0 << endl;
				continue;
			}

			sort(r.begin(),r.end(),std::greater<int>());
			sort(b.begin(),b.end(),std::greater<int>());

			int ans = 0;
			FOR(j,0,small)
				ans += r[j] + b[j] -2;

			cout << ans << endl;
		}
	}
};


int main() {
	Main m;
	m.run();
	return 0;
}
