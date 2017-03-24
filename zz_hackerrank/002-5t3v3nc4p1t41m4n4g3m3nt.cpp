// code may not work

#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

struct Order {
  
  Order( int _price, int _size, char _dir ) : price(_price), size(_size), dir( _dir) {}
  
  int price;
  int size;
  char dir;
};

int getClearingPrice( const std::vector< Order >& orders ) {
    
    std::vector< Order > buy_orders;
    std::vector< Order > sell_orders;
    
    for (Order order : orders) {
        if (order.dir == 'B') {
            buy_orders.push_back (order);
        }
        else if (order.dir == 'S') {
            sell_orders.push_back (order);
        }
    }
    
    // sort buy_orders by desc price
    std::sort(buy_orders.begin(), buy_orders.end(),
              [] (Order const& o1, Order const& o2) { return o1.price > o2.price; });
    
    // sort sell_orders by asc price
    std::sort(sell_orders.begin(), sell_orders.end(),
              [] (Order const& o1, Order const& o2) { return o1.price < o2.price; });
    
    // while someone is willing to
    // buy at a higher price than 
    // someone else is willing to sell,
    // trade on
    // since we're looking for the minimum
    // clearing pice, always trade at the sell price
    
    if (buy_orders.size() == 0 || sell_orders.size() == 0) {
        return 0;
    }
    
    int b = 0;
    int s = 0;
    
    int units_traded = 0;
    int price_of_last_trade;
    
    Order buy_order = buy_orders[b];
    Order sell_order = sell_orders[s];
    
    while (b < buy_orders.size() && s < sell_orders.size()) {
        
        buy_order = buy_orders[b];
        sell_order = sell_orders[s];
        
        if (!(buy_order.price >= sell_order.price)) { break; }
        
        // trade the maximum number of units possible
            
        if (buy_order.size > sell_order.size) {
            // the entire sell order is filled
            units_traded = sell_order.size;
            s += 1;
        }
        else if (buy_order.size == sell_order.size) {
            // both orders are filled
            units_traded = sell_order.size;
            b += 1;
            s += 1;
        }
        else {
            // the entire buy order is filled
            units_traded = buy_order.size;
            b += 1;
        }
        buy_order.size -= units_traded;
        sell_order.size -= units_traded;
        price_of_last_trade = sell_order.price;
    }
    
    return price_of_last_trade;
}

int main() {
    
    std::vector< Order > orders;    
    
    Order a(1,400,'B');
    orders.push_back( a );
    // Order b(2,300,'B');
    // orders.push_back( b );
    // Order c(3,200,'B');
    // orders.push_back( c );
    // Order d(4,100,'B');
    // orders.push_back( d );
    // Order e(5,0,'B');
    // orders.push_back( e );
    // Order f(5,400,'S');
    // orders.push_back( f );
    // Order g(4,300,'S');
    // orders.push_back( g );
    // Order h(3,200,'S');
    // orders.push_back( h );
    // Order i(2,100,'S');
    // orders.push_back( i );
    Order j(1,0,'S');
    orders.push_back( j );
    
    getClearingPrice( orders );
    
    return 0;
}