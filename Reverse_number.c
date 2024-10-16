#include <stdio.h>

int main() {
    int num, reversedNum = 0, remainder;

    // Ask the user for input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Reverse the number
    while (num != 0) {
        remainder = num % 10; // Get the last digit
        reversedNum = reversedNum * 10 + remainder; // Build the reversed number
        num /= 10; // Remove the last digit
    }

    // Display the reversed number
    printf("Reversed Number: %d\n", reversedNum);
    return 0;
}
