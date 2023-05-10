#include<iostream>
using namespace std;

int partition(int arr[], int start, int end) {
    int left=start-1;
    int pivot=end;
    for (int i; i<end; i++) {

    }

}
int quickSort(int arr[], int start, int end){
    int pivotPlace = partition(arr, start, end);
    quickSort(arr, start, pivotPlace-1);
    quickSort(arr, pivotPlace+1, end);
}
int main() {
    
    return 0;
}