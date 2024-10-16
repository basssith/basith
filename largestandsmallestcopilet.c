#include <stdio.h>

void findLargestAndSmallest(int arr[], int n, int *largest, int *smallest) {
    *largest = arr[0];
    *smallest = arr[0];

    for (int i = 1; i < n; i++) {
        if (arr[i] > *largest) {
            *largest = arr[i];
        }
        if (arr[i] < *smallest) {
            *smallest = arr[i];
        }
    }
}

int main() {
    int arr[] = {23, 89, 6, 45, 77, 12, 39};
    int n = sizeof(arr)/sizeof(arr[0]);
    int largest, smallest;

    findLargestAndSmallest(arr, n, &largest, &smallest);

    printf("Largest number: %d\n", largest);
    printf("Smallest number: %d\n", smallest);

    return 0;
}
