#include <iostream>
using namespace std;

int main() {
  int x, y, z;
  cin >> x >> y >> z;
  
  if (x==y && x==z && y==z){
      cout << 3;
  }
  else if (x==y || x==z || y==z){
      cout << 2;
  }
  else {
      cout << 0;
  }
    
  return 0;
}