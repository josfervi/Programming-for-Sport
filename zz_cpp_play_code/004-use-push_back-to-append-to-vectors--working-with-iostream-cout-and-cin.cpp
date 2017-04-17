#include <vector>
#include <iostream>
using namespace std;

int main() {
  
  vector<double> student_marks;
  double mark;
  char answer;
  
  cout << "Enter marks (y/n)? " << flush;
  cin >> answer;
  
  while (answer == 'y' || answer == 'Y') {
    cout << "Enter value: " << flush;
    cin >> mark;
    
    // like python list.append(item)
    student_marks.push_back (mark);
    
    cout << "More students (y/n)? " << flush;
    cin >> answer;
  }

  return 0;
}