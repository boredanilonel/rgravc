#include <stdio.h>

int calculate(int a, int b)
{
    return a + b;
}

int main()
{
    int s;
    s = calculate(5, 6);
    printf("%d", s);
    return 0;
}