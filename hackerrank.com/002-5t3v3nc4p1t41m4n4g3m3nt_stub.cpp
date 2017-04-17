// stub
// incomplete

#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;

//---------------------------------------------

struct Order {
    Order( int _price, int _size, char _dir ) : price(_price), size(_size), dir( _dir) {}
  int price;
  int size;
  char dir;
};

int getClearingPrice( const std::vector< Order > &orders ) {

}
//---------------------------------------------

int main() {
    
   
   int price;
    int size;
    char dir;
    
    std::vector< Order > orders;
    while( cin >> price >> size >> dir ) {
       Order a( price, size, dir );
       orders.push_back(a);
   
    }
    if( orders.back().dir == 'a' ) {
        orders.clear();
        srand(0);
        for( int i = 0;i< 1000000; ++i ) {
         Order a( rand() % 100, rand() %500, i%2 == 0 ? 'B': 'S' );
              orders.push_back( a);
        }
    }
    if( orders.back().dir == 'b' ) {
        orders.clear();
        srand(0);
        for( int i = 0;i< 10000000; ++i ) {
         Order a( rand() % 100, rand() %500, i%2 == 0 ? 'B': 'S' );
              orders.push_back( a);
        }
    }
    if( orders.back().dir == 'c' ) {
        orders.clear();
        srand(100);
        for( int i = 0;i< 1000; ++i ) {
         Order a( rand() % 100, rand() %500, i%2 == 0 ? 'B': 'S' );
              orders.push_back( a);
        }
    }
    cout << getClearingPrice( orders );
    
    return 0;
}

}