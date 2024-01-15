#include <iostream>
using namespace std;
 
void printTwoRepeatNumber(int arr[], int size)
{
    int i, j;
    cout << "Repeating elements are ";
    for (i = 0; i < size; i++) {
        for (j = i + 1; j < size; j++) {
            if (arr[i] == arr[j]) {
                cout << arr[i] << " ";
                break;
            }
        }
    }
}
 
int main()
{
    int arr[] = { 4, 2, 4, 5, 2, 3, 1 };
    int arr_size = sizeof(arr) / sizeof(arr[0]);
   
    printTwoRepeatNumber(arr, arr_size);
    return 0;
}