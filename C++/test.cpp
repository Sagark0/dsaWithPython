#include <iostream>
using namespace std;

int myFunc(int &a) {
    a+=1;
    return 0;
}
int main() {
    int a=1;
    // int* b= &a;
    cout << "before " << a << endl;
    myFunc(a);
    cout << "after " << a << endl;
    // cout << "Address of a " << *b;

    return 0;
}