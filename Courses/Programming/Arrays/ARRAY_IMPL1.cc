#include <iostream> // cout
#include <vector>
using namespace std;

vector<int> performOps(vector<int> A) {
    vector<int> B(2 * A.size(), 0);
    for (int i = 0; i < A.size(); i++) {
        B[i] = A[i];
        B[i + A.size()] = A[(A.size() - i) % A.size()];
    }
    return B;
}

int main() {
  vector<int> A(4,0);
  A[0]=  5;
  A[1]= 10;
  A[2]=  2;
  A[3]=  1;
  vector<int> B = performOps(A);
  for (int i = 0; i < B.size(); i++) {
    cout<<B[i]<<" ";
  }
}