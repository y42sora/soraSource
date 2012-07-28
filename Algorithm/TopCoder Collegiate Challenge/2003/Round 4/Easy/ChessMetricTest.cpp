#include "ChessMetric.h"
#include <iostream>
#include <vector>

using std::cerr;
using std::cout;
using std::endl;
using std::vector;

class ChessMetricTest {

    static void assertEquals(int testCase, const long long& expected, const long long& actual) {
        if (expected == actual) {
            cout << "Test case " << testCase << " PASSED!" << endl;
        } else {
            cout << "Test case " << testCase << " FAILED! Expected: <" << expected << "> but was: <" << actual << '>' << endl;
        }
    }

    ChessMetric solution;

    void testCase0() {
		int size = 3;
        int start_[] = {0, 0};
        vector<int> start(start_, start_ + (sizeof(start_) / sizeof(start_[0])));
        int end_[] = {1, 0};
        vector<int> end(end_, end_ + (sizeof(end_) / sizeof(end_[0])));
		int numMoves = 1;
		long long expected_ = 1LL;
        assertEquals(0, expected_, solution.howMany(size, start, end, numMoves));
    }

    void testCase1() {
		int size = 3;
        int start_[] = {0, 0};
        vector<int> start(start_, start_ + (sizeof(start_) / sizeof(start_[0])));
        int end_[] = {1, 2};
        vector<int> end(end_, end_ + (sizeof(end_) / sizeof(end_[0])));
		int numMoves = 1;
		long long expected_ = 1LL;
        assertEquals(1, expected_, solution.howMany(size, start, end, numMoves));
    }

    void testCase2() {
		int size = 3;
        int start_[] = {0, 0};
        vector<int> start(start_, start_ + (sizeof(start_) / sizeof(start_[0])));
        int end_[] = {2, 2};
        vector<int> end(end_, end_ + (sizeof(end_) / sizeof(end_[0])));
		int numMoves = 1;
		long long expected_ = 0LL;
        assertEquals(2, expected_, solution.howMany(size, start, end, numMoves));
    }

    void testCase3() {
		int size = 3;
        int start_[] = {0, 0};
        vector<int> start(start_, start_ + (sizeof(start_) / sizeof(start_[0])));
        int end_[] = {0, 0};
        vector<int> end(end_, end_ + (sizeof(end_) / sizeof(end_[0])));
		int numMoves = 2;
		long long expected_ = 5LL;
        assertEquals(3, expected_, solution.howMany(size, start, end, numMoves));
    }

    void testCase4() {
		int size = 100;
        int start_[] = {0, 0};
        vector<int> start(start_, start_ + (sizeof(start_) / sizeof(start_[0])));
        int end_[] = {0, 99};
        vector<int> end(end_, end_ + (sizeof(end_) / sizeof(end_[0])));
		int numMoves = 50;
		long long expected_ = 243097320072600LL;
        assertEquals(4, expected_, solution.howMany(size, start, end, numMoves));
    }

    public: void runTest(int testCase) {
        switch (testCase) {
            case (0): testCase0(); break;
            case (1): testCase1(); break;
            case (2): testCase2(); break;
            case (3): testCase3(); break;
            case (4): testCase4(); break;
            default: cerr << "No such test case: " << testCase << endl; break;
        }
    }

};

int main() {
    for (int i = 0; i < 5; i++) {
        ChessMetricTest test;
        test.runTest(i);
    }
}
