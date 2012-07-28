#include "BadNeighbors.h"
#include <iostream>
#include <vector>

using std::cerr;
using std::cout;
using std::endl;
using std::vector;

class BadNeighborsTest {

    static void assertEquals(int testCase, const int& expected, const int& actual) {
        if (expected == actual) {
            cout << "Test case " << testCase << " PASSED!" << endl;
        } else {
            cout << "Test case " << testCase << " FAILED! Expected: <" << expected << "> but was: <" << actual << '>' << endl;
        }
    }

    BadNeighbors solution;

    void testCase0() {
        int donations_[] = {10, 3, 2, 5, 7, 8};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 19;
        assertEquals(0, expected_, solution.maxDonations(donations));
    }

    void testCase1() {
        int donations_[] = {11, 15};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 15;
        assertEquals(1, expected_, solution.maxDonations(donations));
    }

    void testCase2() {
        int donations_[] = {7, 7, 7, 7, 7, 7, 7};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 21;
        assertEquals(2, expected_, solution.maxDonations(donations));
    }

    void testCase3() {
        int donations_[] = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 16;
        assertEquals(3, expected_, solution.maxDonations(donations));
    }

    void testCase4() {
        int donations_[] = {94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72, 37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 2926;
        assertEquals(4, expected_, solution.maxDonations(donations));
    }

    void testCase5() {
        int donations_[] = {10,1,1,1,1,10};
        vector<int> donations(donations_, donations_ + (sizeof(donations_) / sizeof(donations_[0])));
		int expected_ = 12;
        assertEquals(5, expected_, solution.maxDonations(donations));
    }

    public: void runTest(int testCase) {
        switch (testCase) {
            case (0): testCase0(); break;
            case (1): testCase1(); break;
            case (2): testCase2(); break;
            case (3): testCase3(); break;
            case (4): testCase4(); break;
            case (5): testCase5(); break;
            default: cerr << "No such test case: " << testCase << endl; break;
        }
    }

};

int main() {
    for (int i = 0; i < 6; i++) {
        BadNeighborsTest test;
        test.runTest(i);
    }
}
